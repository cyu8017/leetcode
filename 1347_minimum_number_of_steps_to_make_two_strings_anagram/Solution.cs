// LeetCode 1347 - Minimum Number Of Steps To Make Two Strings Anagram
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

public class Solution {
    public int MinSteps(string s, string t) {
        var cnt = new int[26];
        foreach (char c in s) cnt[c - 'a']++;
        foreach (char c in t) cnt[c - 'a']--;
        int answer = 0;
        foreach (int v in cnt) if (v > 0) answer += v;
        return answer;
    }
}
