// LeetCode 3470 - Permutations IV
// https://leetcode.com/problems/permutations-iv/

var permute = function(n, k) {
    const fact = new Array(n + 1);
    fact[0] = 1n;
    for (let i = 1; i <= n; i++) {
        fact[i] = fact[i - 1] * BigInt(i);
        if (fact[i] > 10n ** 18n) fact[i] = 10n ** 18n + 1n;
    }
    const used = new Array(n + 1).fill(false);
    const ans = [];
    let kk = BigInt(k);
    const dfs = (pos) => {
        if (pos === n) return true;
        for (let x = 1; x <= n; x++) {
            if (used[x]) continue;
            if (pos > 0 && (ans[pos - 1] % 2 === x % 2)) continue;
            const rem = n - pos - 1;
            const cnt = fact[rem];
            if (cnt >= kk) {
                used[x] = true;
                ans.push(x);
                if (dfs(pos + 1)) return true;
                ans.pop();
                used[x] = false;
            } else {
                kk -= cnt;
            }
        }
        return false;
    };
    if (!dfs(0)) return [];
    return ans;
};
