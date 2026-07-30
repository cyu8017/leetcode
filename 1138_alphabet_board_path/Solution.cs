// LeetCode 1138 - Alphabet Board Path
// https://leetcode.com/problems/alphabet-board-path/

using System.Text;

public class Solution {
    public string AlphabetBoardPath(string target) {
        int row = 0, col = 0;
        var ans = new StringBuilder();
        foreach (char ch in target) {
            int r = (ch - 'a') / 5, c = (ch - 'a') % 5;
            while (row > r) { ans.Append('U'); row--; }
            while (col > c) { ans.Append('L'); col--; }
            while (row < r) { ans.Append('D'); row++; }
            while (col < c) { ans.Append('R'); col++; }
            ans.Append('!');
        }
        return ans.ToString();
    }
}
