// LeetCode 1138 - Alphabet Board Path
// https://leetcode.com/problems/alphabet-board-path/

class Solution {
    public String alphabetBoardPath(String target) {
        int row = 0, col = 0;
        StringBuilder ans = new StringBuilder();
        for (char ch : target.toCharArray()) {
            int r = (ch - 'a') / 5, c = (ch - 'a') % 5;
            // Move U/L before D/R to avoid falling off 'z'
            while (row > r) { ans.append('U'); row--; }
            while (col > c) { ans.append('L'); col--; }
            while (row < r) { ans.append('D'); row++; }
            while (col < c) { ans.append('R'); col++; }
            ans.append('!');
        }
        return ans.toString();
    }
}
