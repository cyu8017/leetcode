// LeetCode 3403 - Find the Lexicographically Largest String From the Box I
// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/

public class Solution {
    public string AnswerString(string word, int numFriends) {
        if (numFriends == 1) return word;
        int n = word.Length;
        int maxLen = n - (numFriends - 1);
        string ans = "";
        for (int i = 0; i < n; i++) {
            int end = i + maxLen;
            if (end > n) end = n;
            string cand = word.Substring(i, end - i);
            if (string.CompareOrdinal(cand, ans) > 0) ans = cand;
        }
        return ans;
    }
}
