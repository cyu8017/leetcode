// LeetCode 2657 - Find the Prefix Common Array of Two Arrays
// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

var findThePrefixCommonArray = function(A, B) {
    const n = A.length;
    const seenA = new Array(n + 1).fill(false);
    const seenB = new Array(n + 1).fill(false);
    const ans = new Array(n);
    let common = 0;
    for (let i = 0; i < n; i++) {
        if (seenB[A[i]]) common++;
        seenA[A[i]] = true;
        if (seenA[B[i]]) common++;
        seenB[B[i]] = true;
        ans[i] = common;
    }
    return ans;
};
