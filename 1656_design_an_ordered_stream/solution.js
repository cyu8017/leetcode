// LeetCode 1656 - Design an Ordered Stream
// https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream {
    /**
     * @param {number} n
     */
    constructor(n) {
        this.a = Array(n + 1).fill(null);
        this.p = 1;
    }

    /**
     * @param {number} idKey
     * @param {string} value
     * @return {string[]}
     */
    insert(idKey, value) {
        this.a[idKey] = value;
        const out = [];
        while (this.p < this.a.length && this.a[this.p] !== null) {
            out.push(this.a[this.p]);
            this.p++;
        }
        return out;
    }
}

module.exports = { OrderedStream };
