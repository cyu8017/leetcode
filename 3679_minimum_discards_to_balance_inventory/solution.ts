// LeetCode 3679 - Minimum Discards to Balance Inventory
// https://leetcode.com/problems/minimum-discards-to-balance-inventory/

export function minArrivalsToDiscard(arrivals: any, w: any, m: any): any {
    const cnt = new Map();
    const n = arrivals.length;
    const marked = new Array(n).fill(0);
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const x = arrivals[i];
        if (i >= w) cnt.set(arrivals[i - w], (cnt.get(arrivals[i - w]) || 0) - marked[i - w]);
        if ((cnt.get(x) || 0) >= m) ans++;
        else {
            marked[i] = 1;
            cnt.set(x, (cnt.get(x) || 0) + 1);
        }
    }
    return ans;
}
