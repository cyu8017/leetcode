// LeetCode 0875 - Koko Eating Bananas
// https://leetcode.com/problems/koko-eating-bananas/

/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
    let lo = 1, hi = 0;
    for (const p of piles) hi = Math.max(hi, p);
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        let hours = 0;
        for (const p of piles) hours += Math.floor((p + mid - 1) / mid);
        if (hours <= h) hi = mid;
        else lo = mid + 1;
    }
    return lo;
};
