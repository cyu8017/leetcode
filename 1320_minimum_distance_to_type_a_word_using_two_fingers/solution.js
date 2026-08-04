// LeetCode 1320 - Minimum Distance To Type A Word Using Two Fingers
// https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

/**
 * @param {string} word
 * @return {number}
 */
var minimumDistance = function(word) {
    const distance = (a, b) => {
        if (a === 26) return 0;
        return Math.abs(Math.floor(a / 6) - Math.floor(b / 6)) + Math.abs(a % 6 - b % 6);
    };
    const letters = [...word].map((ch) => ch.charCodeAt(0) - 65);
    let dp = new Map([[26, 0]]);
    let previous = letters[0];
    for (let i = 1; i < letters.length; i++) {
        const current = letters[i];
        const nxt = new Map();
        for (const [free, cost] of dp) {
            nxt.set(free, Math.min(nxt.get(free) ?? 1e9, cost + distance(previous, current)));
            nxt.set(previous, Math.min(nxt.get(previous) ?? 1e9, cost + distance(free, current)));
        }
        dp = nxt;
        previous = current;
    }
    return Math.min(...dp.values());
};
