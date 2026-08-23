// LeetCode 0686 - Repeated String Match
// https://leetcode.com/problems/repeated-string-match/

using System.Text;

public class Solution {
    public int RepeatedStringMatch(string a, string b) {
        int repeats = (b.Length + a.Length - 1) / a.Length;
        var built = new StringBuilder(a.Length * (repeats + 1));
        for (int i = 0; i < repeats; i++) built.Append(a);
        if (built.ToString().Contains(b)) return repeats;
        built.Append(a);
        if (built.ToString().Contains(b)) return repeats + 1;
        return -1;
    }
}
