// LeetCode 3330 - Find the Original Typed String I
// https://leetcode.com/problems/find-the-original-typed-string-i/

public class Solution {
    public int PossibleStringCount(string word) {
        int ans = 1;
        for (int i = 1; i < word.Length; i++) {
            if (word[i] == word[i - 1]) ans++;
        }
        return ans;
    }
}
