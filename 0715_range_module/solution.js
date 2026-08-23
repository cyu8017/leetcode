// LeetCode 0715 - Range Module
// https://leetcode.com/problems/range-module/

class RangeModule {
    constructor() {
        this.intervals = [];
    }

    /**
     * @param {number} left
     * @param {number} right
     * @return {void}
     */
    addRange(left, right) {
        const next = [];
        let placed = false;
        for (const iv of this.intervals) {
            const start = iv[0], end = iv[1];
            if (end < left) next.push([start, end]);
            else if (right < start) {
                if (!placed) { next.push([left, right]); placed = true; }
                next.push([start, end]);
            } else {
                left = Math.min(left, start);
                right = Math.max(right, end);
            }
        }
        if (!placed) next.push([left, right]);
        this.intervals = next;
    }

    /**
     * @param {number} left
     * @param {number} right
     * @return {boolean}
     */
    queryRange(left, right) {
        for (const iv of this.intervals) {
            if (iv[0] <= left && right <= iv[1]) return true;
            if (iv[1] >= right) break;
        }
        return false;
    }

    /**
     * @param {number} left
     * @param {number} right
     * @return {void}
     */
    removeRange(left, right) {
        const next = [];
        for (const iv of this.intervals) {
            const start = iv[0], end = iv[1];
            if (end <= left || right <= start) next.push([start, end]);
            else {
                if (start < left) next.push([start, left]);
                if (right < end) next.push([right, end]);
            }
        }
        this.intervals = next;
    }
}
