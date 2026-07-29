// LeetCode 1044 - Longest Duplicate Substring
// https://leetcode.com/problems/longest-duplicate-substring/

function longestDupSubstring(s: string): string {
    const MOD = (1n << 61n) - 1n;
    const BASE = 256n;
    const n = s.length;
    const nums = Array.from(s, (c) => BigInt(c.charCodeAt(0)));

    const search = (length: number): number => {
        if (length === 0) return 0;
        let h = 0n;
        for (let i = 0; i < length; i++) h = (h * BASE + nums[i]) % MOD;
        const seen = new Map<bigint, number[]>();
        seen.set(h, [0]);
        let power = 1n;
        for (let i = 0; i < length; i++) power = (power * BASE) % MOD;
        for (let i = 1; i <= n - length; i++) {
            h = (h * BASE - nums[i - 1] * power + nums[i + length - 1]) % MOD;
            if (h < 0n) h += MOD;
            const cur = s.slice(i, i + length);
            if (seen.has(h)) {
                for (const j of seen.get(h)!) {
                    if (s.slice(j, j + length) === cur) return i;
                }
                seen.get(h)!.push(i);
            } else {
                seen.set(h, [i]);
            }
        }
        return -1;
    };

    let lo = 0, hi = n - 1, start = -1, bestLen = 0;
    while (lo <= hi) {
        const mid = Math.floor((lo + hi) / 2);
        const pos = search(mid);
        if (pos >= 0) {
            start = pos;
            bestLen = mid;
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return start >= 0 ? s.slice(start, start + bestLen) : '';
}
