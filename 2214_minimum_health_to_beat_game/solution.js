// LeetCode 2214 - Minimum Health to Beat Game
// https://leetcode.com/problems/minimum-health-to-beat-game/

/**
 * @param {number[]} damage
 * @param {number} armor
 * @return {number}
 */
var minimumHealth = function(damage, armor) {
    let sum = 0, mx = 0;
    for (const d of damage) { sum += d; mx = Math.max(mx, d); }
    return sum - Math.min(armor, mx) + 1;
};
