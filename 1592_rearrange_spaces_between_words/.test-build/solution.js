"use strict";
// LeetCode 1592 - Rearrange Spaces Between Words
// https://leetcode.com/problems/rearrange-spaces-between-words/
// @ts-nocheck
function reorderSpaces(text) {
    const words = text.trim().split(/\s+/).filter(Boolean);
    let spaces = 0;
    for (const ch of text)
        if (ch === " ")
            spaces++;
    if (words.length === 1)
        return words[0] + " ".repeat(spaces);
    const between = Math.floor(spaces / (words.length - 1));
    const trailing = spaces % (words.length - 1);
    return words.join(" ".repeat(between)) + " ".repeat(trailing);
}
