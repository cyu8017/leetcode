// LeetCode 0822 - Card Flipping Game
// https://leetcode.com/problems/card-flipping-game/

/**
 * @param {number[]} fronts
 * @param {number[]} backs
 * @return {number}
 */
var flipgame = function(fronts, backs) {
    const same = new Set();
    for (let i = 0; i < fronts.length; i++) {
        if (fronts[i] === backs[i]) same.add(fronts[i]);
    }
    let best = Number.MAX_SAFE_INTEGER;
    for (const x of fronts) if (!same.has(x)) best = Math.min(best, x);
    for (const x of backs) if (!same.has(x)) best = Math.min(best, x);
    return best === Number.MAX_SAFE_INTEGER ? 0 : best;
};
