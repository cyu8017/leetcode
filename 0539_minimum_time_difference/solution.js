// LeetCode 0539 - Minimum Time Difference
// https://leetcode.com/problems/minimum-time-difference/

class Solution {
    findMinDifference(timePoints) {
        const minutes = timePoints.map((time) => {
            const [hour, minute] = time.split(":").map(Number);
            return hour * 60 + minute;
        });
        minutes.sort((a, b) => a - b);

        let best = minutes[minutes.length - 1] - minutes[0];
        for (let i = 1; i < minutes.length; i++) {
            best = Math.min(best, minutes[i] - minutes[i - 1]);
        }
        return Math.min(best, 24 * 60 - minutes[minutes.length - 1] + minutes[0]);
    }
}

module.exports = { Solution };
