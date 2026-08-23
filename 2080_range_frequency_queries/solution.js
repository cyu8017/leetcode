// LeetCode 2080 - Range Frequency Queries
// https://leetcode.com/problems/range-frequency-queries/

class RangeFreqQuery {
    /**
     * @param {number[]} arr
     */
    constructor(arr) {
        this.pos = new Map();
        for (let i = 0; i < arr.length; i++) {
            if (!this.pos.has(arr[i])) this.pos.set(arr[i], []);
            this.pos.get(arr[i]).push(i);
        }
    }

    lower(p, x) {
        let lo = 0, hi = p.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (p[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    upper(p, x) {
        let lo = 0, hi = p.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (p[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    /**
     * @param {number} left
     * @param {number} right
     * @param {number} value
     * @return {number}
     */
    query(left, right, value) {
        const p = this.pos.get(value);
        if (!p) return 0;
        return this.upper(p, right) - this.lower(p, left);
    }
}
