// LeetCode 1138 - Alphabet Board Path
// https://leetcode.com/problems/alphabet-board-path/

/**
 * @param {string} target
 * @return {string}
 */
var alphabetBoardPath = function(target) {
    let row = 0, col = 0;
    const ans = [];
    for (const ch of target) {
        const code = ch.charCodeAt(0) - 97;
        const r = Math.floor(code / 5), c = code % 5;
        if (r < row) {
            for (let i = 0; i < row - r; i++) ans.push("U");
            row = r;
        }
        if (c < col) {
            for (let i = 0; i < col - c; i++) ans.push("L");
            col = c;
        }
        if (c > col) {
            for (let i = 0; i < c - col; i++) ans.push("R");
            col = c;
        }
        if (r > row) {
            for (let i = 0; i < r - row; i++) ans.push("D");
            row = r;
        }
        ans.push("!");
    }
    return ans.join("");
};
