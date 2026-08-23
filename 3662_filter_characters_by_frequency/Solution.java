// LeetCode 3662 - Filter Characters by Frequency
// https://leetcode.com/problems/filter-characters-by-frequency/

class Solution {
    public String filterCharacters(String s, int k) {
        int[] cnt = new int[26];
        for (char c : s.toCharArray()) cnt[c - 'a']++;
        StringBuilder ans = new StringBuilder();
        for (char c : s.toCharArray())
            if (cnt[c - 'a'] < k) ans.append(c);
        return ans.toString();
    }
}
