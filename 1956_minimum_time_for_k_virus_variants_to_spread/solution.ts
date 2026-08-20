// LeetCode 1956 - Minimum Time For K Virus Variants to Spread
// https://leetcode.com/problems/minimum-time-for-k-virus-variants-to-spread/

function minDayskVariants(points: number[][], k: number): number {
    let ans = Infinity;
    for (let x = 1; x <= 100; x++) {
        for (let y = 1; y <= 100; y++) {
            const dists = points.map(([px, py]: any) => Math.abs(px - x) + Math.abs(py - y)).sort((a, b: any) => a - b);
            ans = Math.min(ans, dists[k - 1]);
        }
    }
    return ans;
}
