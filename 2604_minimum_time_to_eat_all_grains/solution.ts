// LeetCode 2604 - Minimum Time to Eat All Grains
// https://leetcode.com/problems/minimum-time-to-eat-all-grains/

export function minimumTime(hens: number[], grains: number[]): number {
    hens.sort((a, b) => a - b);
    grains.sort((a, b) => a - b);
    const ok = (t) => {
        let j = 0;
        for (const h of hens) {
            if (j >= grains.length) return true;
            if (grains[j] >= h) {
                while (j < grains.length && grains[j] - h <= t) j++;
            } else {
                if (h - grains[j] > t) return false;
                const left = h - grains[j];
                const maxRight1 = t - 2 * left;
                const maxRight2 = Math.floor((t - left) / 2);
                let reach = h;
                if (maxRight1 > maxRight2) {
                    if (maxRight1 > 0) reach = h + maxRight1;
                } else {
                    if (maxRight2 > 0) reach = h + maxRight2;
                }
                while (j < grains.length && grains[j] <= reach) j++;
            }
        }
        return j >= grains.length;
    };
    let lo = 0, hi = 2000000000;
    while (lo < hi) {
        const mid = lo + Math.floor((hi - lo) / 2);
        if (ok(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
