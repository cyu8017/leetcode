// LeetCode 0422 - Valid Word Square
// https://leetcode.com/problems/valid-word-square/

public class Solution {
    public bool ValidWordSquare(string[] words) {
        for (int row = 0; row < words.Length; row++) {
            string word = words[row];
            for (int col = 0; col < word.Length; col++) {
                if (col >= words.Length || row >= words[col].Length || words[col][row] != word[col]) {
                    return false;
                }
            }
        }
        return true;
    }
}
