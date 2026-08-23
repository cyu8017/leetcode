// LeetCode 3746 - Minimum String Length After Balanced Removals
// https://leetcode.com/problems/minimum-string-length-after-balanced-removals/

var minLengthAfterRemovals = function(s) {
    let a = 0;
    for (const c of s) if (c === 'a') a++;
    const b = s.length - a;
    return Math.abs(a - b);
};
