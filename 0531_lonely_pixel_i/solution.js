// LeetCode 0531 - Lonely Pixel I
// https://leetcode.com/problems/lonely-pixel-i/

class Solution {
    findLonelyPixel(picture) {
        const rows = picture.length;
        const cols = picture[0].length;
        const rowCounts = picture.map((row) => row.filter((cell) => cell === "B").length);
        const colCounts = Array.from({ length: cols }, (_, c) =>
            picture.reduce((count, row) => count + (row[c] === "B" ? 1 : 0), 0)
        );

        let lonely = 0;
        for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {
                if (picture[r][c] === "B" && rowCounts[r] === 1 && colCounts[c] === 1) {
                    lonely += 1;
                }
            }
        }
        return lonely;
    }
}

module.exports = { Solution };
