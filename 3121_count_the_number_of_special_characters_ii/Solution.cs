// LeetCode 3121 - Count the Number of Special Characters II
// https://leetcode.com/problems/count-the-number-of-special-characters-ii/

public class Solution {
    public int NumberOfSpecialChars(string word) {
        int[] first = new int[128], last = new int[128];
        for (int i = 0; i < word.Length; i++) {
            char c = word[i];
            if (first[c] == 0) first[c] = i + 1;
            last[c] = i + 1;
        }
        int ans = 0;
        for (int i = 0; i < 26; i++) {
            if (last['a' + i] > 0 && last['a' + i] < first['A' + i]) ans++;
        }
        return ans;
    }
}
