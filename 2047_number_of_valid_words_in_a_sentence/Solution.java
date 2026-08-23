// LeetCode 2047 - Number of Valid Words in a Sentence
// https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

class Solution {
    public int countValidWords(String sentence) {
        int ans = 0;
        for (String tok : sentence.split(" "))
            if (valid(tok)) ans++;
        return ans;
    }

    private boolean valid(String w) {
        if (w.length() == 0) return false;
        int hyphen = 0;
        for (int i = 0; i < w.length(); i++) {
            char c = w.charAt(i);
            if (c >= '0' && c <= '9') return false;
            if (c == '-') {
                hyphen++;
                if (hyphen > 1 || i == 0 || i == w.length() - 1) return false;
                if (w.charAt(i - 1) < 'a' || w.charAt(i - 1) > 'z' || w.charAt(i + 1) < 'a' || w.charAt(i + 1) > 'z') return false;
            } else if (c == '!' || c == '.' || c == ',') {
                if (i != w.length() - 1) return false;
            } else if (c < 'a' || c > 'z') return false;
        }
        return true;
    }
}
