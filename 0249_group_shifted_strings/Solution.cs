// LeetCode 0249 - Group Shifted Strings
// https://leetcode.com/problems/group-shifted-strings/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<IList<string>> GroupStrings(string[] strings) {
        Dictionary<string, List<string>> groups = new Dictionary<string, List<string>>();
        List<string> order = new List<string>();

        foreach (string text in strings) {
            string key;
            if (text.Length == 0) {
                key = "";
            } else {
                int baseCode = text[0];
                key = string.Join(",", text.Select(ch => ((ch - baseCode + 26) % 26).ToString()));
            }
            if (!groups.ContainsKey(key)) {
                groups[key] = new List<string>();
                order.Add(key);
            }
            groups[key].Add(text);
        }

        return order.Select(key => (IList<string>)groups[key]).ToList();
    }
}
