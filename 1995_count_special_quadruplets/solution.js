// LeetCode 1995 - Count Special Quadruplets
// https://leetcode.com/problems/count-special-quadruplets/

/**
 * @param {number[]} nums
 * @return {number}
 */
var countQuadruplets = function(nums) {
    const n = nums.length;
    let ans = 0;
    for (let a = 0; a < n; a++) {
        for (let b = a + 1; b < n; b++) {
            for (let c = b + 1; c < n; c++) {
                const s = nums[a] + nums[b] + nums[c];
                for (let d = c + 1; d < n; d++) if (nums[d] === s) ans++;
            }
        }
    }
    return ans;
};
