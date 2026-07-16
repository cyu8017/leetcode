// LeetCode 0495 - Teemo Attacking
// https://leetcode.com/problems/teemo-attacking/

class Solution {
    findPoisonedDuration(timeSeries, duration) {
        if (!timeSeries.length) return 0;
        let total = duration;
        for (let index = 1; index < timeSeries.length; index += 1) {
            total += Math.min(duration, timeSeries[index] - timeSeries[index - 1]);
        }
        return total;
    }
}

module.exports = { Solution };
