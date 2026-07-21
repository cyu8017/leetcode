// LeetCode 1812 - Determine Color of a Chessboard Square
// https://leetcode.com/problems/determine-color-of-a-chessboard-square/

/**
 * @param {string} coordinates
 * @return {boolean}
 */
var squareIsWhite = function(coordinates) {
    const col = coordinates.charCodeAt(0) - 'a'.charCodeAt(0) + 1;
    const row = Number(coordinates[1]);
    return (col + row) % 2 === 1;
};
