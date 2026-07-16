// LeetCode 0488 - Zuma Game
// https://leetcode.com/problems/zuma-game/

export class Solution {
    findMinStep(board: string, hand: string): number {
        const shrink = (s: string): string => {
            let i = 0;
            while (i < s.length) {
                let j = i;
                while (j < s.length && s[j] === s[i]) j += 1;
                if (j - i >= 3) return shrink(s.slice(0, i) + s.slice(j));
                i = j;
            }
            return s;
        };

        const memo = new Map<string, number>();
        const dfs = (b: string, h: string): number => {
            const key = `${b}|${h}`;
            if (memo.has(key)) return memo.get(key) as number;
            b = shrink(b);
            if (!b) {
                memo.set(key, 0);
                return 0;
            }
            let best = Infinity;
            for (let i = 0; i <= b.length; i += 1) {
                for (let j = 0; j < h.length; j += 1) {
                    const color = h[j];
                    if (i < b.length && b[i] === color) {
                        // continue
                    } else if (i > 0 && b[i - 1] === color) {
                        // continue
                    } else {
                        continue;
                    }
                    const newB = shrink(b.slice(0, i) + color + b.slice(i));
                    if (newB === b) continue;
                    const newH = h.slice(0, j) + h.slice(j + 1);
                    const steps = dfs(newB, newH);
                    if (steps !== Infinity) best = Math.min(best, steps + 1);
                }
            }
            memo.set(key, best);
            return best;
        };

        const result = dfs(board, hand);
        return result === Infinity ? -1 : result;
    }
}
