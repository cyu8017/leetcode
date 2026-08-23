// LeetCode 2135 - Count Words Obtained After Adding a Letter
// https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

public class Solution {
    public int WordCount(string[] startWords, string[] targetWords) {
        int Mask(string w) {
            int m = 0;
            foreach (char c in w) m |= 1 << (c - 'a');
            return m;
        }
        var have = new HashSet<int>();
        foreach (string w in startWords) have.Add(Mask(w));
        int ans = 0;
        foreach (string w in targetWords) {
            int m = Mask(w);
            for (int i = 0; i < w.Length; i++) {
                if (have.Contains(m ^ (1 << (w[i] - 'a')))) { ans++; break; }
            }
        }
        return ans;
    }
}
