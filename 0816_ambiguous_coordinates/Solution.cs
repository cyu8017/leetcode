// LeetCode 0816 - Ambiguous Coordinates
// https://leetcode.com/problems/ambiguous-coordinates/

using System.Collections.Generic;

public class Solution {
    public IList<string> AmbiguousCoordinates(string s) {
        string digits = s.Substring(1, s.Length - 2);
        List<string> Candidates(string frag) {
            var options = new List<string>();
            if (frag.Length == 0 || (frag.Length > 1 && frag[0] == '0' && frag[^1] == '0')) return options;
            if (frag[0] == '0' && frag.Length > 1) {
                if (frag[^1] != '0') options.Add("0." + frag.Substring(1));
                return options;
            }
            options.Add(frag);
            if (frag[^1] == '0') return options;
            for (int i = 1; i < frag.Length; i++) options.Add(frag.Substring(0, i) + "." + frag.Substring(i));
            return options;
        }
        var answer = new List<string>();
        for (int i = 1; i < digits.Length; i++) {
            foreach (string left in Candidates(digits.Substring(0, i)))
                foreach (string right in Candidates(digits.Substring(i)))
                    answer.Add("(" + left + ", " + right + ")");
        }
        return answer;
    }
}
