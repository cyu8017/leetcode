// LeetCode 2451 - Odd String Difference
// https://leetcode.com/problems/odd-string-difference/

using System.Text;

public class Solution {
    public string OddString(string[] words) {
        string Diff(string w) {
            var b = new StringBuilder();
            for (int i = 1; i < w.Length; i++) {
                int d = w[i] - w[i - 1];
                b.Append((char)(d + 128));
                b.Append(',');
            }
            return b.ToString();
        }
        string d0 = Diff(words[0]), d1 = Diff(words[1]);
        if (d0 == d1) {
            for (int i = 2; i < words.Length; i++) {
                if (Diff(words[i]) != d0) return words[i];
            }
        }
        if (Diff(words[2]) == d0) return words[1];
        return words[0];
    }
}
