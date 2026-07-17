// LeetCode 1756 - Design Most Recently Used Queue
// https://leetcode.com/problems/design-most-recently-used-queue/

class MRUQueue {
    private q: number[];

    constructor(n: number) {
        this.q = [];
        for (let i = 1; i <= n; i++) {
            this.q.push(i);
        }
    }

    fetch(k: number): number {
        const val = this.q.splice(k - 1, 1)[0];
        this.q.push(val);
        return val;
    }
}

export { MRUQueue };
