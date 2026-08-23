// LeetCode 0981 - Time Based Key-Value Store
// https://leetcode.com/problems/time-based-key-value-store/

class TimeMap {
    constructor() {
        this.times = new Map();
        this.vals = new Map();
    }

    /**
     * @param {string} key
     * @param {string} value
     * @param {number} timestamp
     * @return {void}
     */
    set(key, value, timestamp) {
        if (!this.times.has(key)) {
            this.times.set(key, []);
            this.vals.set(key, []);
        }
        this.times.get(key).push(timestamp);
        this.vals.get(key).push(value);
    }

    /**
     * @param {string} key
     * @param {number} timestamp
     * @return {string}
     */
    get(key, timestamp) {
        const tarr = this.times.get(key);
        if (!tarr) return "";
        const varr = this.vals.get(key);
        let lo = 0, hi = tarr.length - 1, ans = -1;
        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if (tarr[mid] <= timestamp) { ans = mid; lo = mid + 1; }
            else hi = mid - 1;
        }
        return ans < 0 ? "" : varr[ans];
    }
}
