// LeetCode 0421 - Maximum XOR of Two Numbers in an Array
// https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution {
    findMaximumXOR(nums) {
        const maximum = Math.max(...nums);
        const maxBit = maximum.toString(2).length;
        const root = {};
        let best = 0;

        for (const number of nums) {
            let node = root;
            for (let bit = maxBit - 1; bit >= 0; bit -= 1) {
                const current = (number >> bit) & 1;
                if (!(current in node)) node[current] = {};
                node = node[current];
            }
        }

        for (const number of nums) {
            let node = root;
            let candidate = 0;
            for (let bit = maxBit - 1; bit >= 0; bit -= 1) {
                const current = (number >> bit) & 1;
                const target = 1 - current;
                if (target in node) {
                    candidate |= 1 << bit;
                    node = node[target];
                } else {
                    node = node[current];
                }
            }
            best = Math.max(best, candidate);
        }

        return best;
    }
}

module.exports = { Solution };
