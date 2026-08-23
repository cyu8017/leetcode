// LeetCode 3760 - Maximum Substrings With Distinct Start
// https://leetcode.com/problems/maximum-substrings-with-distinct-start/

class Solution {
    public int maxDistinct(String s) {
        int[] cnt = new int[26];
        int ans = 0;
        for (char c : s.toCharArray()) {
            cnt[c - 'a']++;
            if (cnt[c - 'a'] == 1) ans++;
        }
        return ans;
    }
}
