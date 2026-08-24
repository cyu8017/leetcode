// LeetCode 0952 - Largest Component Size by Common Factor
// https://leetcode.com/problems/largest-component-size-by-common-factor/

export function largestComponentSize(nums: number[]): number {
    let mx = 0;
    for (const x of nums) mx = Math.max(mx, x);
    const parent = Array.from({ length: mx + 1 }, (_, i) => i);
    const find = (x) => (parent[x] === x ? x : (parent[x] = find(parent[x])));
    const unite = (a, b) => { parent[find(a)] = find(b); };
    const factors = (x) => {
        const res = [];
        for (let d = 2; d * d <= x; d++) {
            if (x % d === 0) {
                res.push(d);
                while (x % d === 0) x = Math.floor(x / d);
            }
        }
        if (x > 1) res.push(x);
        return res;
    };
    for (const num of nums)
        for (const f of factors(num)) unite(num, f);
    const cnt = new Map();
    let ans = 0;
    for (const num of nums) {
        const r = find(num);
        const c = (cnt.get(r) || 0) + 1;
        cnt.set(r, c);
        ans = Math.max(ans, c);
    }
    return ans;
}
