// LeetCode 3838 - Weighted Word Mapping
// https://leetcode.com/problems/weighted-word-mapping/

using System.Text;

public class Solution {
    public string MapWordWeights(string[] words, int[] weights) {
        var ans = new StringBuilder();
        foreach (var w in words) {
            int s = 0;
            foreach (char c in w) s = (s + weights[c - 'a']) % 26;
            ans.Append((char)('a' + (25 - s)));
        }
        return ans.ToString();
    }
}
