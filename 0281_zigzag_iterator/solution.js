// LeetCode 0281 - Zigzag Iterator
// https://leetcode.com/problems/zigzag-iterator/

class ZigzagIterator {
    /**
     * @param {number[]} v1
     * @param {number[]} v2
     */
    constructor(v1, v2) {
        this.vectors = [v1, v2];
        this.indices = [0, 0];
        this.turn = 0;
    }

    /**
     * @return {number}
     */
    next() {
        while (this.indices[this.turn] >= this.vectors[this.turn].length) {
            this.turn = 1 - this.turn;
        }
        const value = this.vectors[this.turn][this.indices[this.turn]];
        this.indices[this.turn] += 1;
        this.turn = 1 - this.turn;
        return value;
    }

    /**
     * @return {boolean}
     */
    hasNext() {
        return this.indices.some((index, vectorIndex) => index < this.vectors[vectorIndex].length);
    }
}

module.exports = { ZigzagIterator };
