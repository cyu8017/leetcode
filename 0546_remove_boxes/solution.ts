// LeetCode 0546 - Remove Boxes
// https://leetcode.com/problems/remove-boxes/

export class Solution {
    removeBoxes(boxes: number[]): number {
        const memo = new Map<string, number>();

        const dp = (left: number, right: number, streak: number): number => {
            if (left > right) return 0;
            const cacheKey = `${left},${right},${streak}`;
            if (memo.has(cacheKey)) return memo.get(cacheKey)!;

            let r = right;
            let s = streak;
            while (r > left && boxes[r] === boxes[r - 1]) {
                r -= 1;
                s += 1;
            }

            let best = (s + 1) ** 2 + dp(left, r - 1, 0);
            for (let i = left; i < r; i++) {
                if (boxes[i] === boxes[r]) {
                    best = Math.max(best, dp(left, i, s + 1) + dp(i + 1, r - 1, 0));
                }
            }

            memo.set(cacheKey, best);
            return best;
        };

        return dp(0, boxes.length - 1, 0);
    }
}
