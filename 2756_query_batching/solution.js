// LeetCode 2756 - Query Batching
// https://leetcode.com/problems/query-batching/

/**
 * @param {Function} queryMultiple
 * @param {number} t
 */
class QueryBatcher {
    constructor(queryMultiple, t) {
        this.queryMultiple = queryMultiple;
        this.t = t;
        this.pending = [];
        this.busyUntil = 0;
        this.timer = null;
    }

    /**
     * @param {string} key
     * @returns {Promise<string>}
     */
    async getValue(key) {
        return new Promise((resolve) => {
            const now = Date.now();
            this.pending.push({key, resolve});
            if (now >= this.busyUntil) {
                this.flush();
            } else if (!this.timer) {
                this.timer = setTimeout(() => {
                    this.timer = null;
                    this.flush();
                }, this.busyUntil - now);
            }
        });
    }

    flush() {
        if (!this.pending.length) return;
        const batch = this.pending;
        this.pending = [];
        if (this.timer) {
            clearTimeout(this.timer);
            this.timer = null;
        }
        this.busyUntil = Date.now() + this.t;
        const keys = batch.map((b) => b.key);
        this.queryMultiple(keys).then((values) => {
            for (let i = 0; i < batch.length; i++) batch[i].resolve(values[i]);
        });
    }
}
