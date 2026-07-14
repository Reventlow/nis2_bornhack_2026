#!/usr/bin/env python3
"""Apply the deploy/ compose specs to the ZimaOS board.

Idempotent: re-applies deploy/asking-why.yml (updating the app and
re-pulling :latest) and installs deploy/watchtower.yml if no app on
the board already runs a watchtower image.

Credentials come from the environment — never stored in this repo:

    ZIMAOS_API_URL   e.g. http://10.19.78.72
    ZIMAOS_USERNAME
    ZIMAOS_PASSWORD

Usage, from the repo root on a machine that can reach the board:

    python3 scripts/zima-deploy.py
"""

import json
import os
import sys
import urllib.request
from pathlib import Path

API = os.environ.get("ZIMAOS_API_URL", "http://10.19.78.72")


def login() -> str:
    user, pw = os.environ.get("ZIMAOS_USERNAME"), os.environ.get("ZIMAOS_PASSWORD")
    if not (user and pw):
        sys.exit("Set ZIMAOS_USERNAME and ZIMAOS_PASSWORD in the environment.")
    req = urllib.request.Request(
        f"{API}/v1/users/login",
        data=json.dumps({"username": user, "password": pw}).encode(),
        headers={"Content-Type": "application/json"},
    )
    return json.load(urllib.request.urlopen(req, timeout=10))["data"]["token"]["access_token"]


def call(token: str, method: str, path: str, body: bytes | None = None,
         content_type: str = "application/json", accept: str = "application/json") -> str:
    req = urllib.request.Request(
        f"{API}{path}", data=body, method=method,
        headers={"Authorization": token, "Content-Type": content_type, "Accept": accept},
    )
    return urllib.request.urlopen(req, timeout=120).read().decode()


def main() -> None:
    token = login()
    apps = json.loads(call(token, "GET", "/v2/app_management/compose"))["data"]

    # Update (or install) the deck app.
    deck_yaml = Path("deploy/asking-why.yml").read_bytes()
    if "asking-why" in apps:
        print("asking-why:", call(token, "PUT", "/v2/app_management/compose/asking-why",
                                  deck_yaml, "application/yaml"))
    else:
        print("asking-why:", call(token, "POST", "/v2/app_management/compose",
                                  deck_yaml, "application/yaml"))

    # Install watchtower unless some app already runs it (possibly under
    # an auto-generated name).
    for app_id in apps:
        yaml_text = call(token, "GET", f"/v2/app_management/compose/{app_id}",
                         accept="application/yaml")
        if "containrrr/watchtower" in yaml_text:
            print(f"watchtower: already present as app '{app_id}', skipping install")
            return
    wt_yaml = Path("deploy/watchtower.yml").read_bytes()
    print("watchtower:", call(token, "POST", "/v2/app_management/compose",
                              wt_yaml, "application/yaml"))


if __name__ == "__main__":
    main()
