// LeetCode 1231 - Divide Chocolate
// https://leetcode.com/problems/divide-chocolate/

function maximizeSweetness(sweetness: number[], k: number): number {
    let lo = 1, hi = Math.floor(sweetness.reduce((s, v) => s + v, 0) / (k + 1));
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        let pieces = 0, current = 0;
        for (const value of sweetness) {
            current += value;
            if (current >= mid) {
                pieces++;
                current = 0;
            }
        }
        if (pieces >= k + 1) lo = mid + 1;
        else hi = mid - 1;
    }
    return hi;
}
