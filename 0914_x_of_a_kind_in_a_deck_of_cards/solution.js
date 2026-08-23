// LeetCode 0914 - X of a Kind in a Deck of Cards
// https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

/**
 * @param {number[]} deck
 * @return {boolean}
 */
var hasGroupsSizeX = function(deck) {
    const count = new Map();
    for (const x of deck) count.set(x, (count.get(x) || 0) + 1);
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    let g = 0;
    for (const c of count.values()) g = gcd(g, c);
    return g >= 2;
};
