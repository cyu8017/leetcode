// LeetCode 2347 - Best Poker Hand
// https://leetcode.com/problems/best-poker-hand/

/**
 * @param {number[]} ranks
 * @param {character[]} suits
 * @return {string}
 */
var bestHand = function(ranks, suits) {
    if (suits[0] === suits[1] && suits[1] === suits[2] && suits[2] === suits[3] && suits[3] === suits[4])
        return "Flush";
    const cnt = new Map();
    let best = 0;
    for (const r of ranks) {
        const c = (cnt.get(r) || 0) + 1;
        cnt.set(r, c);
        best = Math.max(best, c);
    }
    if (best >= 3) return "Three of a Kind";
    if (best === 2) return "Pair";
    return "High Card";
};
