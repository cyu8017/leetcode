// LeetCode 3007 - Maximum Number That Sum of the Prices Is Less Than or Equal to K
// https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/

var findMaximumNumber = function(k, x) {
    let num = 0n;
    let f;
    function dfs(pos, cnt, limit) {
        if (pos === 0) return BigInt(cnt);
        if (!limit && f[pos][cnt] !== -1n) return f[pos][cnt];
        let ans = 0n;
        const up = limit ? Number((num >> BigInt(pos - 1)) & 1n) : 1;
        for (let i = 0; i <= up; i++) {
            let v = cnt;
            if (i === 1 && pos % x === 0) v++;
            ans += dfs(pos - 1, v, limit && i === up);
        }
        if (!limit) f[pos][cnt] = ans;
        return ans;
    }
    let l = 1n, r = 10n ** 17n;
    while (l < r) {
        const mid = (l + r + 1n) >> 1n;
        num = mid;
        let m = 0;
        for (let t = num; t > 0n; t >>= 1n) m++;
        f = Array.from({length: 65}, () => new Array(65).fill(-1n));
        if (dfs(m, 0, true) <= BigInt(k)) l = mid;
        else r = mid - 1n;
    }
    return Number(l);
};
