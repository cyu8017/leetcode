// LeetCode 1825 - Finding MK Average
// https://leetcode.com/problems/finding-mk-average/

class MKAverage {
    /**
     * @param {number} m
     * @param {number} k
     */
    constructor(m, k) {
        this.m = m;
        this.k = k;
        this.stream = [];
    }

    /**
     * @param {number} num
     * @return {void}
     */
    addElement(num) {
        this.stream.push(num);
    }

    /**
     * @return {number}
     */
    calculateMKAverage() {
        if (this.stream.length < this.m) return -1;
        const window = this.stream.slice(-this.m).sort((a, b) => a - b);
        const middle = window.slice(this.k, window.length - this.k);
        let sum = 0;
        for (const v of middle) sum += v;
        return Math.floor(sum / middle.length);
    }
}

module.exports = { MKAverage };
