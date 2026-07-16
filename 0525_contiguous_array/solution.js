// LeetCode 0525 - Contiguous Array
// https://leetcode.com/problems/contiguous-array/

class Solution {
    findMaxLength(nums) {
        const counts = new Map([[0, -1]]);
        let balance = 0;
        let best = 0;
        for (let index = 0; index < nums.length; index += 1) {
            balance += nums[index] === 1 ? 1 : -1;
            if (counts.has(balance)) best = Math.max(best, index - counts.get(balance));
            else counts.set(balance, index);
        }
        return best;
    }
}

module.exports = { Solution };
