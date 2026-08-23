// LeetCode 3223 - Minimum Length of String After Operations
// https://leetcode.com/problems/minimum-length-of-string-after-operations/

var minimumLength = function(s) {
    const cnt = new Array(26).fill(0);
    for (let i = 0; i < s.length; i++) cnt[s.charCodeAt(i) - 97]++;
    let ans = 0;
    for (const x of cnt) {
        if (x > 0) ans += (x & 1) !== 0 ? 1 : 2;
    }
    return ans;
};
