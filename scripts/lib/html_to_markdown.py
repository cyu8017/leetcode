"""Convert LeetCode problem HTML descriptions to Markdown."""

from __future__ import annotations

import html
import re


def _strip_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text)


def _convert_inline_markup(text: str) -> str:
    text = re.sub(r"<sup>(.*?)</sup>", r"^{\1}", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<sub>(.*?)</sub>", r"_{\1}", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(
        r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
        r"[\2](\1)",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    text = re.sub(
        r"<strong[^>]*>(.*?)</strong>",
        r"**\1**",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    text = re.sub(r"<b>(.*?)</b>", r"**\1**", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<em>(.*?)</em>", r"*\1*", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<i>(.*?)</i>", r"*\1*", text, flags=re.IGNORECASE | re.DOTALL)
    return text


def leetcode_html_to_markdown(content: str) -> str:
    if not content:
        return "_No description available._"

    text = html.unescape(content)
    text = text.replace("\r\n", "\n")

    pre_blocks: list[str] = []
    code_blocks: list[str] = []

    def save_pre(match: re.Match[str]) -> str:
        block = match.group(1)
        block = re.sub(r"<br\s*/?>", "\n", block, flags=re.IGNORECASE)
        block = _convert_inline_markup(block)
        block = _strip_tags(block)
        block = block.replace("\u00a0", " ")
        pre_blocks.append(block.strip("\n"))
        return f"\n@@PRE{len(pre_blocks) - 1}@@\n"

    def save_code(match: re.Match[str]) -> str:
        block = _convert_inline_markup(match.group(1))
        block = _strip_tags(block)
        code_blocks.append(block.strip())
        return f"@@CODE{len(code_blocks) - 1}@@"

    text = re.sub(r"<pre>\s*(.*?)\s*</pre>", save_pre, text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<code>(.*?)</code>", save_code, text, flags=re.IGNORECASE | re.DOTALL)

    text = re.sub(r"<img\b[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = _convert_inline_markup(text)

    text = re.sub(r"<ul>\s*", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</ul>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<ol>\s*", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</ol>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<li>\s*", "- ", text, flags=re.IGNORECASE)
    text = re.sub(r"</li>", "\n", text, flags=re.IGNORECASE)

    text = re.sub(r"<p>\s*&nbsp;\s*</p>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<p>\s*</p>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<p>\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"</p>", "\n\n", text, flags=re.IGNORECASE)

    text = _strip_tags(text)
    text = text.replace("\u00a0", " ")

    for index, block in enumerate(code_blocks):
        text = text.replace(f"@@CODE{index}@@", f"`{block}`")

    for index, block in enumerate(pre_blocks):
        text = text.replace(f"@@PRE{index}@@", f"\n```\n{block}\n```\n")

    text = re.sub(r"\*{3,}", "**", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text.strip()


def parse_hints(raw_hints: str | list | None) -> list[str]:
    if not raw_hints:
        return []

    if isinstance(raw_hints, list):
        hints: list[str] = []
        for item in raw_hints:
            if isinstance(item, str) and item.strip():
                hints.append(leetcode_html_to_markdown(item))
        return hints

    hints = []
    for match in re.finditer(r'"([^"]+)"', str(raw_hints)):
        hint = leetcode_html_to_markdown(html.unescape(match.group(1)))
        if hint:
            hints.append(hint)
    return hints
