// LeetCode 0933 - Number of Recent Calls
// https://leetcode.com/problems/number-of-recent-calls/

export class RecentCounter {
    constructor() {
        this.q = [];
    }

    ping(t: any): any {
        this.q.push(t);
        while (this.q[0] < t - 3000) this.q.shift();
        return this.q.length;
    }
}
