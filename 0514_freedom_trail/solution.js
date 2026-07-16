// LeetCode 0514 - Freedom Trail
// https://leetcode.com/problems/freedom-trail/

class Solution {
    findRotateSteps(ring, key) {
        const positions = new Map();
        for (let index = 0; index < ring.length; index += 1) {
            if (!positions.has(ring[index])) positions.set(ring[index], []);
            positions.get(ring[index]).push(index);
        }
        const memo = new Map();
        const dp = (ringIndex, keyIndex) => {
            const state = `${ringIndex},${keyIndex}`;
            if (memo.has(state)) return memo.get(state);
            if (keyIndex === key.length) return 0;
            let best = Infinity;
            for (const pos of positions.get(key[keyIndex])) {
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

module.exports = { Solution };
