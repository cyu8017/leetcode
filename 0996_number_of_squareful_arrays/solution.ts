// LeetCode 0996 - Number of Squareful Arrays
// https://leetcode.com/problems/number-of-squareful-arrays/

export function numSquarefulPerms(nums: number[]): number {
    const count = new Map();
    for (const x of nums) count.set(x, (count.get(x) || 0) + 1);
    const graph = new Map();
    for (const a of count.keys()) graph.set(a, []);
    for (const a of count.keys()) {
        for (const b of count.keys()) {
            const s = a + b;
            const r = Math.round(Math.sqrt(s));
            if (r * r === s) graph.get(a).push(b);
        }
    }
    let ans = 0;
    const dfs = (x, remain) => {
        if (remain === 0) { ans++; return; }
        for (const y of graph.get(x)) {
            if (count.get(y) > 0) {
                count.set(y, count.get(y) - 1);
                dfs(y, remain - 1);
                count.set(y, count.get(y) + 1);
            }
        }
    };
    for (const x of [...count.keys()]) {
        count.set(x, count.get(x) - 1);
        dfs(x, nums.length - 1);
        count.set(x, count.get(x) + 1);
    }
    return ans;
}
