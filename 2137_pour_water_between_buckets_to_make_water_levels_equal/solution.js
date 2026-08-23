// LeetCode 2137 - Pour Water Between Buckets to Make Water Levels Equal
// https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/

/**
 * @param {number[]} buckets
 * @param {number} loss
 * @return {number}
 */
var equalizeWater = function(buckets, loss) {
    let lo = 0, hi = 0;
    for (const b of buckets) hi = Math.max(hi, b);
    for (let iter = 0; iter < 60; iter++) {
        const mid = (lo + hi) / 2;
        let have = 0, need = 0;
        for (const b of buckets) {
            if (b >= mid) have += b - mid;
            else need += mid - b;
        }
        if (have * (1.0 - loss / 100.0) >= need) lo = mid;
        else hi = mid;
    }
    return lo;
};
