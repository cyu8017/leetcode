"use strict";
// LeetCode 1520 - Maximum Number of Non-Overlapping Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
// @ts-nocheck
function maxNumOfSubstrings(s) {
    const first = {}, last = {};
    for (let i = 0; i < s.length; i++) {
        if (!(s[i] in first))
            first[s[i]] = i;
        last[s[i]] = i;
    }
    const intervals = [];
    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (first[ch] !== i)
            continue;
        let end = last[ch];
        let j = i;
        let valid = true;
        while (j <= end) {
            if (first[s[j]] < i) {
                valid = false;
                break;
            }
            end = Math.max(end, last[s[j]]);
            j++;
        }
        if (valid)
            intervals.push([end, i]);
    }
    intervals.sort((a, b) => a[0] - b[0]);
    const answer = [];
    let previousEnd = -1;
    for (const [end, start] of intervals) {
        if (start > previousEnd) {
            answer.push(s.slice(start, end + 1));
            previousEnd = end;
        }
    }
    return answer.sort((a, b) => a.length - b.length);
}
