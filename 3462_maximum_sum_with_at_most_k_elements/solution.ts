// LeetCode 3462 - Maximum Sum With at Most K Elements
// https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

export function maxSum(grid: any, limits: any, k: any): any {
    const h = [];
    let sum = 0;
    const push = (v) => {
        h.push(v);
        h.sort((a, b) => a - b);
    };
    const poll = () => h.shift();
    for (let i = 0; i < grid.length; i++) {
        const r = grid[i].slice().sort((a, b) => a - b);
        let lim = limits[i];
        if (lim > r.length) lim = r.length;
        for (let j = 0; j < lim; j++) {
            const val = r[r.length - 1 - j];
            push(val);
            sum += val;
            if (h.length > k) sum -= poll();
        }
    }
    return sum;
}
