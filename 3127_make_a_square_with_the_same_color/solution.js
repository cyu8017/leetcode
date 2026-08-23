// LeetCode 3127 - Make a Square with the Same Color
// https://leetcode.com/problems/make-a-square-with-the-same-color/

/**
 * @param {character[][]} grid
 * @return {boolean}
 */
var canMakeSquare = function(grid) {
    const dirs = [0, 0, 1, 1, 0];
    for (let i = 0; i < 2; i++) {
        for (let j = 0; j < 2; j++) {
            let cnt1 = 0, cnt2 = 0;
            for (let k = 0; k < 4; k++) {
                const x = i + dirs[k], y = j + dirs[k + 1];
                if (grid[x][y] === 'W') cnt1++;
                else cnt2++;
            }
            if (cnt1 !== cnt2) return true;
        }
    }
    return false;
};
