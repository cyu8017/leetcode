// LeetCode 3623 - Count Number of Trapezoids I
// https://leetcode.com/problems/count-number-of-trapezoids-i/

export function countTrapezoids(points: any): any {
    const MOD = 1000000007;
    const cnt = new Map();
    for (const p of points) cnt.set(p[1], (cnt.get(p[1]) || 0) + 1);
    let ans = 0, pre = 0;
    for (const c of cnt.values()) {
        const lines = c * (c - 1) / 2;
        ans = (ans + pre * lines) % MOD;
        pre = (pre + lines) % MOD;
    }
    return ans;
}
