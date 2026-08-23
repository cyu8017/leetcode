// LeetCode 0302 - Smallest Rectangle Enclosing Black Pixels
// https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/

/**
 * @param {character[][]} image
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var minArea = function(image, x, y) {
    const rows = image.length;
    const cols = image[0].length;
    const columnHasBlack = (col) => image.some((row) => row[col] === "1");
    const rowHasBlack = (row) => image[row].some((cell) => cell === "1");

    let left = 0;
    let right = y;
    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        if (columnHasBlack(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    const leftBound = left;

    left = y;
    right = cols - 1;
    while (left < right) {
        const mid = Math.floor((left + right + 1) / 2);
        if (columnHasBlack(mid)) {
            left = mid;
        } else {
            right = mid - 1;
        }
    }
    const rightBound = left;

    let top = 0;
    let bottom = x;
    while (top < bottom) {
        const mid = Math.floor((top + bottom) / 2);
        if (rowHasBlack(mid)) {
            bottom = mid;
        } else {
            top = mid + 1;
        }
    }
    const topBound = top;

    top = x;
    bottom = rows - 1;
    while (top < bottom) {
        const mid = Math.floor((top + bottom + 1) / 2);
        if (rowHasBlack(mid)) {
            top = mid;
        } else {
            bottom = mid - 1;
        }
    }
    const bottomBound = top;

    return (rightBound - leftBound + 1) * (bottomBound - topBound + 1);
};
