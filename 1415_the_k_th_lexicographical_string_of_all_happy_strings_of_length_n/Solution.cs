// LeetCode 1415 - The K Th Lexicographical String Of All Happy Strings Of Length N
// https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

using System.Collections.Generic;
public class Solution {
    public string GetHappyString(int n, int k) {
        var answer = new List<string>();
        void Build(string path) {
            if (path.Length == n) { answer.Add(path); return; }
            foreach (char c in "abc")
                if (path.Length == 0 || path[path.Length - 1] != c)
                    Build(path + c);
        }
        Build("");
        return k <= answer.Count ? answer[k - 1] : "";
    }
}
