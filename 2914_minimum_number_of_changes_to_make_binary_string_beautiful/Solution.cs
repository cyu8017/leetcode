// LeetCode 2914 - Minimum Number of Changes to Make Binary String Beautiful
// https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

public class Solution {
    public int MinChanges(string s) {
        int ans = 0;
        for (int i = 0; i < s.Length; i += 2)
            if (s[i] != s[i + 1]) ans++;
        return ans;
    }
}
