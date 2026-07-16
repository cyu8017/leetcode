using System.Collections.Generic;

public class Solution {
    public int LengthOfLongestSubstringTwoDistinct(string s) {
        var counts = new Dictionary<char, int>();
        int left = 0, best = 0;
        for (int right = 0; right < s.Length; right++) {
            counts.TryGetValue(s[right], out int count); counts[s[right]] = count + 1;
            while (counts.Count > 2) {
                char c = s[left++];
                if (--counts[c] == 0) counts.Remove(c);
            }
            best = System.Math.Max(best, right - left + 1);
        }
        return best;
    }
}