// LeetCode 2307 - Check for Contradictions in Equations
// https://leetcode.com/problems/check-for-contradictions-in-equations/

export function checkContradictions(equations: string[][], values: number[]): boolean {
    const parent = new Map();
    const weight = new Map();
    const find = (x) => {
        if (!parent.has(x)) {
            parent.set(x, x);
            weight.set(x, 1.0);
            return x;
        }
        if (parent.get(x) !== x) {
            const p = find(parent.get(x));
            weight.set(x, weight.get(x) * weight.get(parent.get(x)));
            parent.set(x, p);
        }
        return parent.get(x);
    };
    for (let i = 0; i < equations.length; ++i) {
        const a = equations[i][0], b = equations[i][1];
        const ra = find(a), rb = find(b);
        if (ra === rb) {
            if (Math.abs(weight.get(a) / weight.get(b) - values[i]) > 1e-5) return true;
        } else {
            parent.set(ra, rb);
            weight.set(ra, values[i] * weight.get(b) / weight.get(a));
        }
    }
    return false;
}
