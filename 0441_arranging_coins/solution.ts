// LeetCode 0441 - Arranging Coins
// https://leetcode.com/problems/arranging-coins/

export class Solution {
    arrangeCoins(n: number): number {
        let low = 0;
        let high = n;
        while (low <= high) {
            const mid = Math.floor((low + high) / 2);
            if ((mid * (mid + 1)) / 2 <= n) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return high;
    }
}
