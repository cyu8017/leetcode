// LeetCode 2166 - Design Bitset
// https://leetcode.com/problems/design-bitset/

class Bitset {
    /**
     * @param {number} size
     */
    constructor(size) {
        this.size = size;
        this.bits = new Array(size).fill(0);
        this.ones = 0;
        this.flipped = false;
    }

    /**
     * @param {number} idx
     * @return {void}
     */
    fix(idx) {
        const target = this.flipped ? 0 : 1;
        if (this.bits[idx] !== target) {
            this.bits[idx] = target;
            this.ones += this.flipped ? -1 : 1;
        }
    }

    /**
     * @param {number} idx
     * @return {void}
     */
    unfix(idx) {
        const target = this.flipped ? 1 : 0;
        if (this.bits[idx] !== target) {
            this.bits[idx] = target;
            this.ones += this.flipped ? 1 : -1;
        }
    }

    /**
     * @return {void}
     */
    flip() {
        this.flipped = !this.flipped;
        this.ones = this.size - this.ones;
    }

    /**
     * @return {boolean}
     */
    all() { return this.ones === this.size; }

    /**
     * @return {boolean}
     */
    one() { return this.ones > 0; }

    /**
     * @return {number}
     */
    count() { return this.ones; }

    /**
     * @return {string}
     */
    toString() {
        const b = new Array(this.size);
        for (let i = 0; i < this.size; i++) {
            let v = this.bits[i];
            if (this.flipped) v ^= 1;
            b[i] = String(v);
        }
        return b.join('');
    }
}
