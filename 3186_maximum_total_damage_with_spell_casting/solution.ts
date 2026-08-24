// LeetCode 3186 - Maximum Total Damage With Spell Casting
// https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

export function maximumTotalDamage(power: any): any {
    const n = power.length;
    power.sort((a, b) => a - b);
    const cnt = new Map();
    const nxt = new Array(n);
    const f = new Array(n).fill(0);
    const lowerBound = (a, x) => {
        let lo = 0, hi = a.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    for (let i = 0; i < n; i++) {
        cnt.set(power[i], (cnt.get(power[i]) || 0) + 1);
        nxt[i] = lowerBound(power, power[i] + 3);
    }
    const dfs = (i) => {
        if (i >= n) return 0;
        if (f[i] !== 0) return f[i];
        const a = dfs(i + cnt.get(power[i]));
        const b = power[i] * cnt.get(power[i]) + dfs(nxt[i]);
        return (f[i] = Math.max(a, b));
    };
    return dfs(0);
}
