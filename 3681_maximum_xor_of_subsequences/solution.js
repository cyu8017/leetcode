// LeetCode 3681 - Maximum XOR of Subsequences
// https://leetcode.com/problems/maximum-xor-of-subsequences/

var maxXorSubsequences = function(nums) {
    const basis = new Array(32).fill(0);
    for (const x of nums) {
        let cur = x;
        for (let b = 31; b >= 0; b--) {
            if ((cur & (1 << b)) === 0) continue;
            if (basis[b] === 0) {
                basis[b] = cur;
                break;
            }
            cur ^= basis[b];
        }
    }
    let ans = 0;
    for (let b = 31; b >= 0; b--) {
        if ((ans ^ basis[b]) > ans) ans ^= basis[b];
    }
    return ans;
};
