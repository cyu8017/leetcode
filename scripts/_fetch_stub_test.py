#!/usr/bin/env python3
import json
import urllib.request

query = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    title
    codeSnippets { lang langSlug code }
  }
}
"""
body = json.dumps(
    {"query": query, "variables": {"titleSlug": "find-closest-person"}}
).encode()
req = urllib.request.Request(
    "https://leetcode.com/graphql",
    data=body,
    headers={
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://leetcode.com/problems/find-closest-person/",
    },
)
with urllib.request.urlopen(req, timeout=20) as resp:
    data = json.loads(resp.read().decode())
snippets = data["data"]["question"]["codeSnippets"]
for s in snippets:
    if s["langSlug"] in ("golang", "python3"):
        print("====", s["langSlug"])
        print(s["code"])
