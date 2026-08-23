// LeetCode 0451 - Sort Characters By Frequency
// https://leetcode.com/problems/sort-characters-by-frequency/

using System.Collections.Generic;
using System.Linq;
using System.Text;

public class Solution {
    public string FrequencySort(string s) {
        Dictionary<char, int> counts = new();
        foreach (char ch in s) {
            counts[ch] = counts.GetValueOrDefault(ch) + 1;
        }
        StringBuilder result = new();
        foreach (KeyValuePair<char, int> entry in counts.OrderByDescending(kv => kv.Value).ThenBy(kv => kv.Key)) {
            result.Append(new string(entry.Key, entry.Value));
        }
        return result.ToString();
    }
}
