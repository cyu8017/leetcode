// LeetCode 0900 - RLE Iterator
// https://leetcode.com/problems/rle-iterator/

class RLEIterator {
    /**
     * @param {number[]} encoding
     */
    constructor(encoding) {
        this.enc = encoding.slice();
        this.i = 0;
    }

    /**
     * @param {number} n
     * @return {number}
     */
    next(n) {
        while (this.i < this.enc.length) {
            if (this.enc[this.i] >= n) {
                this.enc[this.i] -= n;
                return this.enc[this.i + 1];
            }
            n -= this.enc[this.i];
            this.i += 2;
        }
        return -1;
    }
}

module.exports = { RLEIterator };
