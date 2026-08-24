// LeetCode 2226 - Maximum Candies Allocated to K Children
// https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

/**
 * @param {number[]} candies
 * @param {number} k
 * @return {number}
 */
var maximumCandies = function(candies, k) {
    let mx = 0;
    for (const c of candies) mx = Math.max(mx, c);
    let lo = 0, hi = mx;
    const can = (mid) => {
        if (mid === 0) return true;
        let cnt = 0;
        for (const c of candies) {
            cnt += Math.floor(c / mid);
            if (cnt >= k) return true;
        }
        return false;
    };
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (can(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
};
