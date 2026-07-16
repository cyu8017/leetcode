// LeetCode 0514 - Freedom Trail
// https://leetcode.com/problems/freedom-trail/

export class Solution {
    findRotateSteps(ring: string, key: string): number {
        const positions = new Map<string, number[]>();
        for (let index = 0; index < ring.length; index += 1) {
            if (!positions.has(ring[index])) positions.set(ring[index], []);
            positions.get(ring[index]) as number[].push(index);
        }
        const memo = new Map<string, number>();
        const dp = (ringIndex: number, keyIndex: number): number => {
            const state = `${ringIndex},${keyIndex}`;
            if (memo.has(state)) return memo.get(state) as number;
            if (keyIndex === key.length) return 0;
            let best = Infinity;
            for (const pos of positions.get(key[keyIndex]) as number[]) {
                const clockwise = (pos - ringIndex + ring.length) % ring.length;
                const counter = (ringIndex - pos + ring.length) % ring.length;
                const steps = Math.min(clockwise, counter) + 1;
                best = Math.min(best, steps + dp(pos, keyIndex + 1));
            }
            memo.set(state, best);
            return best;
        };
        return dp(0, 0);
    }
}
