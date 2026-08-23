// LeetCode 1456 - Maximum Number Of Vowels In A Substring Of Given Length
// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution {
    public int maxVowels(String s, int k) {
        int count = 0, ans = 0;
        for (int i = 0; i < s.length(); i++) {
            if (isVowel(s.charAt(i))) count++;
            if (i >= k && isVowel(s.charAt(i - k))) count--;
            if (i >= k - 1) ans = Math.max(ans, count);
        }
        return ans;
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}
