// LeetCode 1552 - Magnetic Force Between Two Balls
// https://leetcode.com/problems/magnetic-force-between-two-balls/

/**
 * @param {number[]} position
 * @param {number} m
 * @return {number}
 */
var maxDistance = function(position, m) {
    position.sort((a, b) => a - b);
    let lo = 1, hi = Math.floor((position[position.length - 1] - position[0]) / (m - 1));
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        let count = 1, last = position[0];
        for (let i = 1; i < position.length; i++) {
            if (position[i] - last >= mid) {
                count++;
                last = position[i];
            }
        }
        if (count >= m) lo = mid + 1;
        else hi = mid - 1;
    }
    return hi;
};
