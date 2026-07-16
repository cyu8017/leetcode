// LeetCode 0533 - Lonely Pixel II
// https://leetcode.com/problems/lonely-pixel-ii/

class Solution {
    findBlackPixel(picture, target) {
        const rows = picture.length;
        const cols = picture[0].length;
        const rowStrings = picture.map((row) => row.join(""));
        const rowCounts = picture.map((row) => row.filter((cell) => cell === "B").length);
        const colCounts = Array.from({ length: cols }, (_, c) =>
            picture.reduce((count, row) => count + (row[c] === "B" ? 1 : 0), 0)
        );

        let lonely = 0;
        for (let r = 0; r < rows; r++) {
            if (rowCounts[r] !== target) continue;
            for (let c = 0; c < cols; c++) {
                if (picture[r][c] !== "B" || colCounts[c] !== target) continue;
                const matches = picture.every(
                    (row, i) => row[c] !== "B" || rowStrings[r] === rowStrings[i]
                );
                if (matches) lonely += 1;
            }
        }
        return lonely;
    }
}

module.exports = { Solution };
