// LeetCode 2631 - Group By
// https://leetcode.com/problems/group-by/

export function groupBy(self: any[], fn: any): any {
    const out = {};
    for (const x of self) {
        const k = fn(x);
        if (!out[k]) out[k] = [];
        out[k].push(x);
    }
    return out;
}
