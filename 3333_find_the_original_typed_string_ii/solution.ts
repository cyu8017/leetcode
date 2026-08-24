// LeetCode 3333 - Find the Original Typed String II
// https://leetcode.com/problems/find-the-original-typed-string-ii/

export function possibleStringCount(word: any, k: any): any {
    const mod = 1000000007;
    const groups = [];
    for (let i = 0; i < word.length; ) {
        let j = i;
        while (j < word.length && word[j] === word[i]) j++;
        groups.push(j - i);
        i = j;
    }
    let total = 1;
    for (const g of groups) total = total * g % mod;
    if (k <= groups.length) return total;
    const need = k - 1;
    let dp = new Array(need).fill(0);
    dp[0] = 1;
    for (const g of groups) {
        const ndp = new Array(need).fill(0);
        const pref = new Array(need + 1).fill(0);
        for (let i = 0; i < need; i++) pref[i + 1] = (pref[i] + dp[i]) % mod;
        for (let s = 0; s < need; s++) {
            let lo = s - g;
            if (lo < 0) lo = 0;
            const hi = s - 1;
            if (hi >= 0) ndp[s] = (pref[hi + 1] - pref[lo] + mod) % mod;
        }
        dp = ndp;
    }
    let bad = 0;
    for (const v of dp) bad = (bad + v) % mod;
    return (total - bad + mod) % mod;
}
