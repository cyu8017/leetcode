// LeetCode 2027 - Minimum Moves to Convert String
// https://leetcode.com/problems/minimum-moves-to-convert-string/

public class Solution {
    public int MinimumMoves(string s) {
        int ans = 0;
        for (int i = 0; i < s.Length; ) {
            if (s[i] == 'X') { ans++; i += 3; }
            else i++;
        }
        return ans;
    }
}
