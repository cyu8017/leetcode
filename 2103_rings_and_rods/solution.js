// LeetCode 2103 - Rings and Rods
// https://leetcode.com/problems/rings-and-rods/

/**
 * @param {string} rings
 * @return {number}
 */
var countPoints = function(rings) {
    const mask = new Array(10).fill(0);
    for (let i = 0; i < rings.length; i += 2) {
        const c = rings[i];
        const r = rings.charCodeAt(i + 1) - 48;
        const bit = c === 'R' ? 1 : c === 'G' ? 2 : 4;
        mask[r] |= bit;
    }
    let ans = 0;
    for (const m of mask) if (m === 7) ans++;
    return ans;
};
