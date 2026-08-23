// LeetCode 3816 - Lexicographically Smallest String After Deleting Duplicate Characters
// https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/

using System.Text;

public class Solution {
    public string LexSmallestAfterDeletion(string s) {
        int[] cnt = new int[26];
        foreach (char c in s) cnt[c - 'a']++;
        var stk = new StringBuilder();
        foreach (char c in s) {
            while (stk.Length > 0 && stk[stk.Length - 1] > c && cnt[stk[stk.Length - 1] - 'a'] > 1) {
                cnt[stk[stk.Length - 1] - 'a']--;
                stk.Length--;
            }
            stk.Append(c);
        }
        while (cnt[stk[stk.Length - 1] - 'a'] > 1) {
            cnt[stk[stk.Length - 1] - 'a']--;
            stk.Length--;
        }
        return stk.ToString();
    }
}
