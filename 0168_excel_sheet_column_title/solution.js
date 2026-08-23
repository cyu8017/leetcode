// LeetCode 0168 - Excel Sheet Column Title
// https://leetcode.com/problems/excel-sheet-column-title/

/**
 * Converts a 1-indexed column number into an Excel column title.
 * @param {number} columnNumber
 * @return {string}
 */
var convertToTitle = function(columnNumber) {
    const characters = [];
    while (columnNumber > 0) {
        columnNumber--;
        characters.push(String.fromCharCode('A'.charCodeAt(0) + (columnNumber % 26)));
        columnNumber = Math.floor(columnNumber / 26);
    }
    return characters.reverse().join('');
};