// LeetCode 1011 - Capacity To Ship Packages Within D Days
// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

function shipWithinDays(weights: number[], days: number): number {
    let lo = Math.max(...weights);
    let hi = weights.reduce((a, b) => a + b, 0);
    const can = (cap: number): boolean => {
        let need = 1, cur = 0;
        for (const w of weights) {
            if (cur + w > cap) {
                need++;
                cur = 0;
            }
            cur += w;
        }
        return need <= days;
    };
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (can(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
