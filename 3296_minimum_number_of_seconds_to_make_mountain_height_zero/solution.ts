// LeetCode 3296 - Minimum Number of Seconds to Make Mountain Height Zero
// https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

function ok(t: any, mountainHeight: any, workerTimes: any): any {
    let total = 0;
    for (const w of workerTimes) {
        let l = 0, h = mountainHeight;
        while (l < h) {
            const mid = Math.floor((l + h + 1) / 2);
            if (w * mid * (mid + 1) / 2 <= t) l = mid;
            else h = mid - 1;
        }
        total += l;
        if (total >= mountainHeight) return true;
    }
    return total >= mountainHeight;
}export function minNumberOfSeconds(mountainHeight: any, workerTimes: any): any {
    let lo = 0, hi = 1e18;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (ok(mid, mountainHeight, workerTimes)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
