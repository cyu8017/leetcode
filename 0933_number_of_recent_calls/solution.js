// LeetCode 0933 - Number of Recent Calls
// https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter {
    constructor() {
        this.q = [];
    }

    /**
     * @param {number} t
     * @return {number}
     */
    ping(t) {
        this.q.push(t);
        while (this.q[0] < t - 3000) this.q.shift();
        return this.q.length;
    }
}

module.exports = { RecentCounter };
