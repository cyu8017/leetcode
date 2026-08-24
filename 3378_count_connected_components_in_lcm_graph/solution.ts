// LeetCode 3378 - Count Connected Components in LCM Graph
// https://leetcode.com/problems/count-connected-components-in-lcm-graph/

function gcd(a: any, b: any): any {
    while (b !== 0) { const t = a % b; a = b; b = t; }
    return a;
}export function countComponents(nums: any, threshold: any): any {
    const n = nums.length;
    const parent = Array.from({length: n}, (_, i) => i);
    const find = (x) => {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    };
    const unite = (a, b) => {
        const ra = find(a), rb = find(b);
        if (ra !== rb) parent[ra] = rb;
    };
    const idx = new Map();
    for (let i = 0; i < n; i++) idx.set(nums[i], i);
    for (let d = 1; d <= threshold; d++) {
        let first = -1;
        for (let m = d; m <= threshold; m += d) {
            if (idx.has(m)) {
                const i = idx.get(m);
                if (first === -1) first = i;
                else if (nums[first] * nums[i] / gcd(nums[first], nums[i]) <= threshold)
                    unite(first, i);
            }
        }
    }
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const a = nums[i], b = nums[j];
            const g = gcd(a, b);
            if ((a / g) * b <= threshold) unite(i, j);
        }
    }
    const comp = new Set();
    for (let i = 0; i < n; i++) comp.add(find(i));
    return comp.size;
}
