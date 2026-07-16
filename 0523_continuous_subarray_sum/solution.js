// LeetCode 0523 - Continuous Subarray Sum
// https://leetcode.com/problems/continuous-subarray-sum/

class Solution {
    checkSubarraySum(nums, k) {
        let prefix = 0;
        const remainders = new Map([[0, -1]]);
        for (let index = 0; index < nums.length; index += 1) {
            prefix += nums[index];
            const mod = k ? prefix % k : prefix;
            if (remainders.has(mod)) {
                if (index - remainders.get(mod) >= 2) return true;
            } else {
                remainders.set(mod, index);
            }
        }
        return false;
    }
}

module.exports = { Solution };
