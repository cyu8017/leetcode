// LeetCode 0532 - K-diff Pairs in an Array
// https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution {
    findPairs(nums, k) {
        if (k < 0) return 0;

        const freq = new Map();
        for (const num of nums) {
            freq.set(num, (freq.get(num) || 0) + 1);
        }

        let pairs = 0;
        for (const num of freq.keys()) {
            if (k === 0) {
                if (freq.get(num) > 1) pairs += 1;
            } else if (freq.has(num + k)) {
                pairs += 1;
            }
        }
        return pairs;
    }
}

module.exports = { Solution };
