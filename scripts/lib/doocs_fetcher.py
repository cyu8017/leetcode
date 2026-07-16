"""Fetch English problem descriptions from the doocs/leetcode GitHub mirror."""

from __future__ import annotations

import html
import re
import urllib.error
import urllib.request
from urllib.parse import quote

DOOCS_RAW_BASE = "https://raw.githubusercontent.com/doocs/leetcode/main"


def doocs_title_variants(title: str) -> list[str]:
    """Return title variants used by doocs/leetcode folder names."""
    title = title.strip()
    variants = [title]
    no_colon = re.sub(r":\s*", " ", title)
    if no_colon not in variants:
        variants.append(no_colon)
    collapsed = re.sub(r"\s+", " ", no_colon).strip()
    if collapsed not in variants:
        variants.append(collapsed)
    return variants


def doocs_readme_url(number: int, title: str) -> str:
    start = (number // 100) * 100
    end = start + 99
    folder = f"{number:04d}.{title}"
    return f"{DOOCS_RAW_BASE}/solution/{start:04d}-{end:04d}/{quote(folder)}/README_EN.md"


def extract_description(markdown: str) -> str:
    markdown = re.sub(r"^---.*?---\s*", "", markdown, flags=re.DOTALL)
    match = re.search(
        r"## Description\s*\n+(.*?)(?=\n## |\Z)",
        markdown,
        flags=re.DOTALL | re.IGNORECASE,
    )
    if not match:
        return ""
    return match.group(1).strip()


def doocs_description_to_markdown(description: str) -> str:
    text = html.unescape(description)
    text = text.replace("\r\n", "\n")
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)

    code_blocks: list[str] = []

    def save_code(match: re.Match[str]) -> str:
        block = match.group(1)
        block = re.sub(r"<sup>(.*?)</sup>", r"^{\1}", block, flags=re.IGNORECASE | re.DOTALL)
        block = re.sub(r"<sub>(.*?)</sub>", r"_{\1}", block, flags=re.IGNORECASE | re.DOTALL)
        block = re.sub(r"<[^>]+>", "", block)
        code_blocks.append(block.strip())
        return f"@@CODE{len(code_blocks) - 1}@@"

    text = re.sub(r"<code>(.*?)</code>", save_code, text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"</?p>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<strong[^>]*>(.*?)</strong>", r"**\1**", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<b>(.*?)</b>", r"**\1**", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<em>(.*?)</em>", r"*\1*", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<sup>(.*?)</sup>", r"^{\1}", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<sub>(.*?)</sub>", r"_{\1}", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<li>\s*", "- ", text, flags=re.IGNORECASE)
    text = re.sub(r"</li>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</?[uo]l>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)

    for index, block in enumerate(code_blocks):
        text = text.replace(f"@@CODE{index}@@", f"`{block}`")

    text = text.replace("\u00a0", " ")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text.strip()


def fetch_doocs_readme_en(number: int, title: str, timeout: int = 30) -> str | None:
    for variant in doocs_title_variants(title):
        url = doocs_readme_url(number, variant)
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "leetcode-solutions-readme-updater"},
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read().decode("utf-8")
        except urllib.error.HTTPError:
            continue
    return None


def fetch_doocs_description(number: int, title: str, timeout: int = 30) -> str | None:
    for variant in doocs_title_variants(title):
        url = doocs_readme_url(number, variant)
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "leetcode-solutions-readme-updater"},
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                markdown = response.read().decode("utf-8")
        except urllib.error.HTTPError:
            continue

        description = extract_description(markdown)
        if len(description) >= 50:
            return doocs_description_to_markdown(description)
    return None
