// LeetCode 0464 - Can I Win
// https://leetcode.com/problems/can-i-win/

export class Solution {
    canIWin(maxChoosableInteger: number, desiredTotal: number): boolean {
        if (desiredTotal <= 0) return true;
        const total = (maxChoosableInteger * (maxChoosableInteger + 1)) / 2;
        if (total < desiredTotal) return false;

        const memo = new Map<number, boolean>();

        const canWin = (state: number, currentTotal: number): boolean => {
            if (memo.has(state)) return memo.get(state)!;
            for (let pick = 1; pick <= maxChoosableInteger; pick += 1) {
                const bit = 1 << (pick - 1);
                if (state & bit) continue;
                if (currentTotal + pick >= desiredTotal) {
                    memo.set(state, true);
                    return true;
                }
                if (!canWin(state | bit, currentTotal + pick)) {
                    memo.set(state, true);
                    return true;
                }
            }
            memo.set(state, false);
            return false;
        };

        return canWin(0, 0);
    }
}
