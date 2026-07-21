// LeetCode 1861 - Rotating the Box
// https://leetcode.com/problems/rotating-the-box/

/**
 * @param {character[][]} boxGrid
 * @return {character[][]}
 */
var rotateTheBox = function(boxGrid) {
    const m = boxGrid.length, n = boxGrid[0].length;
    const rotated = Array.from({ length: n }, () => new Array(m).fill("."));
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            rotated[i][j] = boxGrid[m - 1 - j][i];
        }
    }
    for (let col = 0; col < m; col++) {
        let row = n - 1;
        for (let i = n - 1; i >= 0; i--) {
            if (rotated[i][col] === "*") row = i - 1;
            else if (rotated[i][col] === "#") {
                rotated[i][col] = ".";
                rotated[row][col] = "#";
                row--;
            }
        }
    }
    return rotated;
};
