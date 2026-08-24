// LeetCode 3876 - Construct Uniform Parity Array II
// https://leetcode.com/problems/construct-uniform-parity-array-ii/

var uniformArray = function(nums1) {
    let mn = Infinity;
    for (const x of nums1) {
        if (x % 2 === 1 && x < mn) mn = x;
    }
    for (const x of nums1) {
        if (x % 2 === 0 && mn !== Infinity && x < mn) return false;
    }
    return true;
};
