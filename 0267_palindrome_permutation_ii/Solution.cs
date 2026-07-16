// LeetCode 0267 - Palindrome Permutation II
// https://leetcode.com/problems/palindrome-permutation-ii/

using System.Collections.Generic;
using System.Linq;
using System.Text;

public class Solution {
    public IList<string> GeneratePalindromes(string s) {
        var counts = new Dictionary<char, int>();
        foreach (char ch in s) {
            if (!counts.ContainsKey(ch)) {
                counts[ch] = 0;
            }
            counts[ch]++;
        }

        string middle = "";
        var oddChars = counts.Where(entry => entry.Value % 2 != 0).Select(entry => entry.Key).ToList();
        if (oddChars.Count > 1) {
            return new List<string>();
        }
        if (oddChars.Count == 1) {
            middle = oddChars[0].ToString();
        }

        var half = new List<char>();
        foreach (char ch in counts.Keys.OrderBy(ch => ch)) {
            for (int i = 0; i < counts[ch] / 2; i++) {
                half.Add(ch);
            }
        }

        var result = new List<string>();
        var used = new bool[half.Count];
        var path = new List<char>();

        void Backtrack() {
            if (path.Count == half.Count) {
                string prefix = new string(path.ToArray());
                var reversed = new StringBuilder(prefix.Length);
                for (int i = prefix.Length - 1; i >= 0; i--) {
                    reversed.Append(prefix[i]);
                }
                result.Add(prefix + middle + reversed);
                return;
            }
            for (int index = 0; index < half.Count; index++) {
                if (used[index]) {
                    continue;
                }
                if (index > 0 && half[index] == half[index - 1] && !used[index - 1]) {
                    continue;
                }
                used[index] = true;
                path.Add(half[index]);
                Backtrack();
                path.RemoveAt(path.Count - 1);
                used[index] = false;
            }
        }

        Backtrack();
        return result;
    }
}
