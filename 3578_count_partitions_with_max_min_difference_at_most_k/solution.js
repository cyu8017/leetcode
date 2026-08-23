// LeetCode 3578 - Count Partitions With Max-Min Difference at Most K
// https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

var countPartitions = function(nums, k) {
    const mod = 1000000007;
    const sl = new Map();
    const n = nums.length;
    const f = new Array(n + 1).fill(0), g = new Array(n + 1).fill(0);
    f[0] = g[0] = 1;
    const keys = [];
    function add(v) {
        if (!sl.has(v)) {
            sl.set(v, 0);
            let lo = 0, hi = keys.length;
            while (lo < hi) {
                const mid = (lo + hi) >> 1;
                if (keys[mid] < v) lo = mid + 1;
                else hi = mid;
            }
            keys.splice(lo, 0, v);
        }
        sl.set(v, sl.get(v) + 1);
    }
    function rem(v) {
        const c = sl.get(v) - 1;
        if (c === 0) {
            sl.delete(v);
            const ix = keys.indexOf(v);
            if (ix >= 0) keys.splice(ix, 1);
        } else sl.set(v, c);
    }
    for (let l = 1, r = 1; r <= n; r++) {
        add(nums[r - 1]);
        while (keys[keys.length - 1] - keys[0] > k) {
            rem(nums[l - 1]);
            l++;
        }
        f[r] = g[r - 1];
        if (l >= 2) f[r] = (f[r] - g[l - 2] + mod) % mod;
        g[r] = (g[r - 1] + f[r]) % mod;
    }
    return f[n];
};
