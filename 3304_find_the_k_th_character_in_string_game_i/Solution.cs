// LeetCode 3304 - Find the K-th Character in String Game I
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

using System.Text;

public class Solution {
    public char KthCharacter(int k) {
        var sb = new StringBuilder("a");
        while (sb.Length < k) {
            int n = sb.Length;
            for (int i = 0; i < n; i++) sb.Append((char)('a' + ((sb[i] - 'a' + 1) % 26)));
        }
        return sb[k - 1];
    }
}
