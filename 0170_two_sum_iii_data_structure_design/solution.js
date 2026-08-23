// LeetCode 0170 - Two Sum III - Data structure design
// https://leetcode.com/problems/two-sum-iii-data-structure-design/

/**
 * Stores numbers and checks whether any pair sums to a value.
 */
class TwoSum {
    constructor() {
        this.counts = new Map();
    }

    /**
     * @param {number} number
     * @return {null}
     */
    add(number) {
        this.counts.set(number, (this.counts.get(number) || 0) + 1);
        return null;
    }

    /**
     * @param {number} value
     * @return {boolean}
     */
    find(value) {
        for (const [number, count] of this.counts) {
            const complement = value - number;
            if (complement === number) {
                if (count >= 2) {
                    return true;
                }
            } else if (this.counts.has(complement)) {
                return true;
            }
        }
        return false;
    }
}

module.exports = { TwoSum };