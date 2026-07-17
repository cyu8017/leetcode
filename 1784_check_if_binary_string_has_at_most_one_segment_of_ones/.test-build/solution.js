"use strict";
// LeetCode 1784 - Check if Binary String Has at Most One Segment of Ones
// https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
function checkOnesSegment(s) {
    let start = 0;
    let end = s.length;
    while (start < end && s[start] === '0')
        start++;
    while (end > start && s[end - 1] === '0')
        end--;
    return !s.slice(start, end).includes('01');
}
