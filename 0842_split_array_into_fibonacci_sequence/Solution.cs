// LeetCode 0842 - Split Array into Fibonacci Sequence
// https://leetcode.com/problems/split-array-into-fibonacci-sequence/

using System.Collections.Generic;

public class Solution {
    public IList<int> SplitIntoFibonacci(string num) {
        int n = num.Length;
        var path = new List<int>();
        bool Dfs(int start) {
            if (start == n) return path.Count >= 3;
            long val = 0;
            for (int end = start; end < n; end++) {
                if (num[start] == '0' && end > start) break;
                val = val * 10 + (num[end] - '0');
                if (val > int.MaxValue) break;
                if (path.Count >= 2) {
                    long total = (long)path[^1] + path[^2];
                    if (val < total) continue;
                    if (val > total) break;
                }
                path.Add((int)val);
                if (Dfs(end + 1)) return true;
                path.RemoveAt(path.Count - 1);
            }
            return false;
        }
        Dfs(0);
        return path;
    }
}
