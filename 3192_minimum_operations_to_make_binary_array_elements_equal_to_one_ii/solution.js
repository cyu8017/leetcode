// LeetCode 3192 - Minimum Operations to Make Binary Array Elements Equal to One II
// https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/

var minOperations = function(nums) {
    let ans = 0, v = 0;
    for (const raw of nums) {
        const x = raw ^ v;
        if (x === 0) { v ^= 1; ans++; }
    }
    return ans;
};
