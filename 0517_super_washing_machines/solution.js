// LeetCode 0517 - Super Washing Machines
// https://leetcode.com/problems/super-washing-machines/

class Solution {
    findMinMoves(machines) {
        const total = machines.reduce((sum, value) => sum + value, 0);
        const count = machines.length;
        if (total % count) return -1;
        const target = total / count;
        let prefix = 0;
        let result = 0;
        for (const clothes of machines) {
            const diff = clothes - target;
            prefix += diff;
            result = Math.max(result, Math.abs(prefix), diff);
        }
        return result;
    }
}

module.exports = { Solution };
