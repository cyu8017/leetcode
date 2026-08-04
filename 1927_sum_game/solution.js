// LeetCode 1927 - Sum Game
// https://leetcode.com/problems/sum-game/

/**
 * @param {string} num
 * @return {boolean}
 */
var sumGame = function(num) {
    const half = num.length >> 1;
    const score = (s) => {
        let q = 0, dig = 0;
        for (const c of s) {
            if (c === "?") q++;
            else dig += c.charCodeAt(0) - 48;
        }
        return dig * 2 + q * 9;
    };
    return score(num.slice(0, half)) !== score(num.slice(half));
};
