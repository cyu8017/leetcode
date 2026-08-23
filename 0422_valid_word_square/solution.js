// LeetCode 0422 - Valid Word Square
// https://leetcode.com/problems/valid-word-square/

class Solution {
    validWordSquare(words) {
        for (let row = 0; row < words.length; row += 1) {
            const word = words[row];
            for (let col = 0; col < word.length; col += 1) {
                if (col >= words.length || row >= words[col].length || words[col][row] !== word[col]) {
                    return false;
                }
            }
        }
        return true;
    }
}

module.exports = { Solution };
