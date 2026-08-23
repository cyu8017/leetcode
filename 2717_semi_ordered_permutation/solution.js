// LeetCode 2717 - Semi-Ordered Permutation
// https://leetcode.com/problems/semi-ordered-permutation/

var semiOrderedPermutation = function(nums) {
    const n = nums.length;
    let p1 = 0, pn = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] === 1) p1 = i;
        if (nums[i] === n) pn = i;
    }
    let ans = p1 + (n - 1 - pn);
    if (p1 > pn) ans--;
    return ans;
};
