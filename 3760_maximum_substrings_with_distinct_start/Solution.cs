// LeetCode 3760 - Maximum Substrings With Distinct Start
// https://leetcode.com/problems/maximum-substrings-with-distinct-start/

public class Solution {
    public int MaxDistinct(string s) {
        int[] cnt = new int[26];
        int ans = 0;
        foreach (char c in s) {
            cnt[c - 'a']++;
            if (cnt[c - 'a'] == 1) ans++;
        }
        return ans;
    }
}
