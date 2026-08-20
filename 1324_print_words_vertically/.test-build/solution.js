"use strict";
// LeetCode 1324 - Print Words Vertically
// https://leetcode.com/problems/print-words-vertically/
function printVertically(s) {
    const words = s.split(" ");
    const maxLen = Math.max(...words.map((w) => w.length));
    const answer = [];
    for (let i = 0; i < maxLen; i++) {
        let row = "";
        for (const word of words)
            row += i < word.length ? word[i] : " ";
        answer.push(row.replace(/\s+$/, ""));
    }
    return answer;
}
