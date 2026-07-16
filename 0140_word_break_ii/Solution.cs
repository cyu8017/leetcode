// LeetCode 0140 - Word Break II
// https://leetcode.com/problems/word-break-ii/

using System.Collections.Generic;

public class Solution {
    public IList<string> WordBreak(string s, IList<string> wordDict) {
        var words = new HashSet<string>(wordDict);
        var memo = new Dictionary<int, IList<string>>();
        return Sentences(0);

        IList<string> Sentences(int start) {
            if (memo.TryGetValue(start, out IList<string> cached)) return cached;
            var result = new List<string>();
            if (start == s.Length) result.Add("");
            else for (int end = start + 1; end <= s.Length; end++) {
                string word = s.Substring(start, end - start);
                if (!words.Contains(word)) continue;
                foreach (string tail in Sentences(end)) result.Add(tail.Length == 0 ? word : word + " " + tail);
            }
            memo[start] = result;
            return result;
        }
    }
}
