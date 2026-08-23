// LeetCode 0854 - K-Similar Strings
// https://leetcode.com/problems/k-similar-strings/

using System.Collections.Generic;

public class Solution {
    public int KSimilarity(string s1, string s2) {
        if (s1 == s2) return 0;
        var queue = new Queue<(string, int)>();
        queue.Enqueue((s1, 0));
        var seen = new HashSet<string> { s1 };
        List<string> Neighbors(string s) {
            char[] arr = s.ToCharArray();
            int i = 0;
            while (arr[i] == s2[i]) i++;
            var res = new List<string>();
            for (int j = i + 1; j < arr.Length; j++) {
                if (arr[j] == s2[i] && arr[j] != s2[j]) {
                    (arr[i], arr[j]) = (arr[j], arr[i]);
                    res.Add(new string(arr));
                    (arr[i], arr[j]) = (arr[j], arr[i]);
                }
            }
            return res;
        }
        while (queue.Count > 0) {
            var (cur, dist) = queue.Dequeue();
            foreach (string nxt in Neighbors(cur)) {
                if (nxt == s2) return dist + 1;
                if (seen.Add(nxt)) queue.Enqueue((nxt, dist + 1));
            }
        }
        return -1;
    }
}
