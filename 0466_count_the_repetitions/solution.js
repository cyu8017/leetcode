// LeetCode 0466 - Count The Repetitions
// https://leetcode.com/problems/count-the-repetitions/

class Solution {
    getMaxRepetitions(s1, n1, s2, n2) {
        if (!s2) return 0;

        let index = 0;
        let s2Count = 0;
        const record = new Map();

        for (let repeat = 0; repeat < n1; repeat += 1) {
            for (const char of s1) {
                if (char === s2[index]) {
                    index += 1;
                    if (index === s2.length) {
                        index = 0;
                        s2Count += 1;
                    }
                }
            }
            if (record.has(index)) {
                const [previousRepeat, previousCount] = record.get(index);
                const cycle = repeat - previousRepeat;
                const countCycle = s2Count - previousCount;
                const remaining = n1 - repeat - 1;
                s2Count += Math.floor(remaining / cycle) * countCycle;
                repeat += Math.floor(remaining / cycle) * cycle;
                if (repeat >= n1 - 1) break;
            }
            record.set(index, [repeat, s2Count]);
        }

        return Math.floor(s2Count / n2);
    }
}

module.exports = { Solution };
