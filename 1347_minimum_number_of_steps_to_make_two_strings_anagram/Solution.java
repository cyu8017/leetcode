// LeetCode 1347 - Minimum Number Of Steps To Make Two Strings Anagram
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

class Solution {
    public int minSteps(String s, String t) {
        int[] cnt = new int[26];
        for (int i = 0; i < s.length(); i++) {
            cnt[s.charAt(i) - 'a']++;
            cnt[t.charAt(i) - 'a']--;
        }
        int answer = 0;
        for (int c : cnt) if (c > 0) answer += c;
        return answer;
    }
}
