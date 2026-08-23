// LeetCode 2047 - Number of Valid Words in a Sentence
// https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

public class Solution {
    public int CountValidWords(string sentence) {
        bool Valid(string w) {
            if (w.Length == 0) return false;
            int hyphen = 0;
            for (int i = 0; i < w.Length; i++) {
                char c = w[i];
                if (c >= '0' && c <= '9') return false;
                if (c == '-') {
                    hyphen++;
                    if (hyphen > 1 || i == 0 || i == w.Length - 1) return false;
                    if (w[i - 1] < 'a' || w[i - 1] > 'z' || w[i + 1] < 'a' || w[i + 1] > 'z') return false;
                } else if (c == '!' || c == '.' || c == ',') {
                    if (i != w.Length - 1) return false;
                } else if (c < 'a' || c > 'z') return false;
            }
            return true;
        }
        int ans = 0;
        foreach (var tok in sentence.Split(' ', System.StringSplitOptions.RemoveEmptyEntries))
            if (Valid(tok)) ans++;
        return ans;
    }
}
