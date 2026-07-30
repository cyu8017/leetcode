// LeetCode 1927 - Sum Game
// https://leetcode.com/problems/sum-game/

public class Solution {
    public bool SumGame(string num) {
        int half = num.Length / 2;
        int Score(string s) {
            int q = 0, dig = 0;
            foreach (char c in s) {
                if (c == '?') q++;
                else dig += c - '0';
            }
            return dig * 2 + q * 9;
        }
        return Score(num.Substring(0, half)) != Score(num.Substring(half));
    }
}