// LeetCode 0546 - Remove Boxes
// https://leetcode.com/problems/remove-boxes/

class Solution {
    removeBoxes(boxes) {
        const memo = new Map();

        const key = (left, right, streak) => `${left},${right},${streak}`;

        const dp = (left, right, streak) => {
            if (left > right) return 0;
            const cacheKey = key(left, right, streak);
            if (memo.has(cacheKey)) return memo.get(cacheKey);

            while (right > left && boxes[right] === boxes[right - 1]) {
                right -= 1;
                streak += 1;
            }

            let best = (streak + 1) ** 2 + dp(left, right - 1, 0);
            for (let i = left; i < right; i++) {
                if (boxes[i] === boxes[right]) {
                    best = Math.max(best, dp(left, i, streak + 1) + dp(i + 1, right - 1, 0));
                }
            }

            memo.set(cacheKey, best);
            return best;
        };

        return dp(0, boxes.length - 1, 0);
    }
}

module.exports = { Solution };
