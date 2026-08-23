// LeetCode 3145 - Find Products of Elements of Big Array
// https://leetcode.com/problems/find-products-of-elements-of-big-array/

/**
 * @param {number[][]} queries
 * @return {number[]}
 */
var findProductsOfElements = function(queries) {
    const M = 50;
    const cnt = new Array(M + 1).fill(0);
    const s = new Array(M + 1).fill(0);
    let p = 1n;
    for (let i = 1; i <= M; i++) {
        cnt[i] = cnt[i - 1] * 2n + p;
        s[i] = s[i - 1] * 2n + p * BigInt(i - 1);
        p *= 2n;
    }
    const numIdxAndSum = (x) => {
        let idx = 0n, totalSum = 0n;
        x = BigInt(x);
        while (x > 0n) {
            let i = 0;
            let t = x;
            while (t > 1n) { t >>= 1n; i++; }
            idx += cnt[i];
            totalSum += s[i];
            x -= 1n << BigInt(i);
            totalSum += (x + 1n) * BigInt(i);
            idx += x + 1n;
        }
        return [idx, totalSum];
    };
    const f = (i) => {
        i = BigInt(i);
        let l = 0n, r = 1n << BigInt(M);
        while (l < r) {
            const mid = (l + r + 1n) >> 1n;
            const p = numIdxAndSum(mid);
            if (p[0] < i) l = mid;
            else r = mid - 1n;
        }
        const p = numIdxAndSum(l);
        let totalSum = p[1];
        i -= p[0];
        let x = l + 1n;
        for (let j = 0n; j < i; j++) {
            const y = x & -x;
            let tz = 0n, yy = y;
            while ((yy & 1n) === 0n) { tz++; yy >>= 1n; }
            totalSum += tz;
            x -= y;
        }
        return totalSum;
    };
    const qpow = (a, n, mod) => {
        let ans = 1n % mod;
        a %= mod;
        while (n > 0n) {
            if ((n & 1n) !== 0n) ans = ans * a % mod;
            a = a * a % mod;
            n >>= 1n;
        }
        return ans;
    };
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const left = BigInt(queries[i][0]), right = BigInt(queries[i][1]), mod = BigInt(queries[i][2]);
        const power = f(right + 1n) - f(left);
        ans[i] = Number(qpow(2n, power, mod));
    }
    return ans;
};
