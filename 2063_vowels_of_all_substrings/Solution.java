// LeetCode 2063 - Vowels of All Substrings
// https://leetcode.com/problems/vowels-of-all-substrings/

class Solution {
    public long countVowels(String word) {
        int n = word.length();
        long ans = 0;
        for (int i = 0; i < n; i++)
            if (isVowel(word.charAt(i))) ans += (long) (i + 1) * (n - i);
        return ans;
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}
