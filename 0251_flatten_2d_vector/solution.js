// LeetCode 0251 - Flatten 2D Vector
// https://leetcode.com/problems/flatten-2d-vector/

class Vector2D {
    /**
     * @param {number[][]} vec
     */
    constructor(vec) {
        this.vec = vec;
        this.row = 0;
        this.col = 0;
        this._advance();
    }

    _advance() {
        while (this.row < this.vec.length && this.col >= this.vec[this.row].length) {
            this.row += 1;
            this.col = 0;
        }
    }

    /**
     * @return {number}
     */
    next() {
        const value = this.vec[this.row][this.col];
        this.col += 1;
        this._advance();
        return value;
    }

    /**
     * @return {boolean}
     */
    hasNext() {
        this._advance();
        return this.row < this.vec.length;
    }
}

module.exports = { Vector2D };
