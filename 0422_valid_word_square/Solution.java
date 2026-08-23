// LeetCode 0422 - Valid Word Square
// https://leetcode.com/problems/valid-word-square/

class Solution {
    public boolean validWordSquare(String[] words) {
        for (int row = 0; row < words.length; row++) {
            String word = words[row];
            for (int col = 0; col < word.length(); col++) {
                if (col >= words.length
                        || row >= words[col].length()
                        || words[col].charAt(row) != word.charAt(col)) {
                    return false;
                }
            }
        }
        return true;
    }
}
