// LeetCode 0477 - Total Hamming Distance
// https://leetcode.com/problems/total-hamming-distance/

class Solution {
    totalHammingDistance(nums) {
        let total = 0;
        for (let bit = 0; bit < 32; bit += 1) {
            let zeros = 0;
            let ones = 0;
            for (const value of nums) {
                if (value & (1 << bit)) ones += 1;
                else zeros += 1;
            }
            total += zeros * ones;
        }
        return total;
    }
}

module.exports = { Solution };
