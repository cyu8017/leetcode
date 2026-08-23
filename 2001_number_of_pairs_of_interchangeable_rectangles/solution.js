// LeetCode 2001 - Number of Pairs of Interchangeable Rectangles
// https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

/**
 * @param {number[][]} rectangles
 * @return {number}
 */
var interchangeableRectangles = function(rectangles) {
    const gcd = (a, b) => {
        while (b !== 0) { const t = a % b; a = b; b = t; }
        return a;
    };
    const freq = new Map();
    let ans = 0;
    for (const rect of rectangles) {
        const g = gcd(rect[0], rect[1]);
        const key = (rect[0] / g) + "/" + (rect[1] / g);
        const f = freq.get(key) || 0;
        ans += f;
        freq.set(key, f + 1);
    }
    return ans;
};
