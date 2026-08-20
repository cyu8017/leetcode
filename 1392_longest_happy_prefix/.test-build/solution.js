"use strict";
// LeetCode 1392: Longest Happy Prefix
function longestPrefix(s) {
    const lps = Array(s.length).fill(0);
    for (let i = 1, length = 0; i < s.length;) {
        if (s[i] === s[length])
            lps[i++] = ++length;
        else if (length)
            length = lps[length - 1];
        else
            i++;
    }
    return s.slice(0, lps[s.length - 1]);
}
