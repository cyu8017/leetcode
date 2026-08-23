// LeetCode 3406 - Find the Lexicographically Largest String From the Box II
// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-ii/

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
