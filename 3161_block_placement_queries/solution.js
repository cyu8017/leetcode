// LeetCode 3161 - Block Placement Queries
// https://leetcode.com/problems/block-placement-queries/

/**
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var getResults = function(queries) {
    function FenwickMax(n) {
        this.vals = new Array(n + 1).fill(0);
    }
    FenwickMax.prototype.maximize = function(i, val) {
        for (; i < this.vals.length; i += i & -i)
            this.vals[i] = Math.max(this.vals[i], val);
    };
    FenwickMax.prototype.get = function(i) {
        let res = 0;
        for (; i > 0; i -= i & -i) res = Math.max(res, this.vals[i]);
        return res;
    };
    const lowerBound = (a, x) => {
        let lo = 0, hi = a.length;
        while (lo < hi) {
            const mid = Math.floor((lo + hi) / 2);
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    let n = queries.length * 3;
    if (n > 50000) n = 50000;
    const tree = new FenwickMax(n + 1);
    const obs = [0, n];
    for (const q of queries) {
        if (q[0] === 1) {
            const x = q[1];
            const idx = lowerBound(obs, x);
            if (idx === obs.length || obs[idx] !== x) obs.splice(idx, 0, x);
        }
    }
    for (let i = 0; i + 1 < obs.length; i++) {
        tree.maximize(obs[i + 1], obs[i + 1] - obs[i]);
    }
    const ans = [];
    for (let i = queries.length - 1; i >= 0; i--) {
        const typ = queries[i][0], x = queries[i][1];
        if (typ === 1) {
            const j = lowerBound(obs, x);
            const prev = obs[j - 1], next = obs[j + 1];
            obs.splice(j, 1);
            tree.maximize(next, next - prev);
        } else {
            const sz = queries[i][2];
            const j = lowerBound(obs, x + 1) - 1;
            const prev = obs[j];
            ans.push(tree.get(prev) >= sz || x - prev >= sz);
        }
    }
    ans.reverse();
    return ans;
};
