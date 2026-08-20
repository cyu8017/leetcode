// LeetCode 1923 - Longest Common Subpath
// https://leetcode.com/problems/longest-common-subpath/

function longestCommonSubpath(n: number, paths: number[][]): number {
    const BASE1 = 911382323n, MOD1 = 1000000007n;
    const BASE2 = 972663749n, MOD2 = 1000000009n;
    const modPow = (base: any, exp: any, mod: any) => {
        let r = 1n, b = base, e = BigInt(exp);
        while (e > 0n) {
            if (e & 1n) r = r * b % mod;
            b = b * b % mod;
            e >>= 1n;
        }
        return r;
    };
    const hasCommon = (length: any) => {
        if (length === 0) return true;
        let common = null;
        const pow1 = modPow(BASE1, length, MOD1);
        const pow2 = modPow(BASE2, length, MOD2);
        for (const path of paths) {
            if (path.length < length) return false;
            let h1 = 0n, h2 = 0n;
            const seen = new Set();
            for (let i = 0; i < path.length; i++) {
                h1 = (h1 * BASE1 + BigInt(path[i] + 1)) % MOD1;
                h2 = (h2 * BASE2 + BigInt(path[i] + 1)) % MOD2;
                if (i >= length) {
                    h1 = (h1 - BigInt(path[i - length] + 1) * pow1 % MOD1 + MOD1) % MOD1;
                    h2 = (h2 - BigInt(path[i - length] + 1) * pow2 % MOD2 + MOD2) % MOD2;
                }
                if (i >= length - 1) seen.add(`${h1},${h2}`);
            }
            if (common === null) common = seen;
            else {
                const next = new Set();
                for (const x of common) if (seen.has(x)) next.add(x);
                common = next;
            }
            if (!common.size) return false;
        }
        return true;
    };
    let lo = 0, hi = Math.min(...paths.map((p: any[]) => p.length));
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (hasCommon(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}
