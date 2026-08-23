// LeetCode 3316 - Find Maximum Removals From Source String
// https://leetcode.com/problems/find-maximum-removals-from-source-string/

public class Solution {
    public int MaxRemovals(string source, string pattern, int[] targetIndices) {
        int n = source.Length;
        bool Ok(int removeFirst) {
            bool[] mark = new bool[n];
            for (int i = 0; i < removeFirst; i++) mark[targetIndices[i]] = true;
            int j = 0;
            for (int i = 0; i < n && j < pattern.Length; i++) {
                if (mark[i]) continue;
                if (source[i] == pattern[j]) j++;
            }
            return j == pattern.Length;
        }
        int lo = 0, hi = targetIndices.Length;
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (Ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}
