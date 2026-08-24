// LeetCode 3645 - Maximum Total from Optimal Activation Order
// https://leetcode.com/problems/maximum-total-from-optimal-activation-order/

export function maxTotal(value: any, limit: any): any {
    const g = new Map();
    for (let i = 0; i < value.length; i++) {
        if (!g.has(limit[i])) g.set(limit[i], []);
        g.get(limit[i]).push(value[i]);
    }
    let ans = 0;
    for (const [lim, vs] of g) {
        vs.sort((a, b) => b - a);
        for (let i = 0; i < Math.min(lim, vs.length); i++) ans += vs[i];
    }
    return ans;
}
