// LeetCode 3775 - Reverse Words With Same Vowel Count
// https://leetcode.com/problems/reverse_words_with_same_vowel_count/

class Solution {
    private int calc(String w) {
        int cnt = 0;
        for (char c : w.toCharArray()) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') cnt++;
        }
        return cnt;
    }

    public String reverseWords(String s) {
        String[] words = s.trim().split("\\s+");
        int cnt = calc(words[0]);
        StringBuilder ans = new StringBuilder();
        ans.append(words[0]);
        for (int i = 1; i < words.length; i++) {
            String w = words[i];
            if (calc(w) == cnt) w = new StringBuilder(w).reverse().toString();
            ans.append(' ').append(w);
        }
        return ans.toString();
    }
}
