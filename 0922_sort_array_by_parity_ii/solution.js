// LeetCode 0922 - Sort Array By Parity II
// https://leetcode.com/problems/sort-array-by-parity-ii/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParityII = function(nums) {
    const n = nums.length;
    const ans = new Array(n);
    let even = 0, odd = 1;
    for (const x of nums) {
        if (x % 2 === 0) { ans[even] = x; even += 2; }
        else { ans[odd] = x; odd += 2; }
    }
    return ans;
};
