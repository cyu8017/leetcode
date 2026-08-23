// LeetCode 3316 - Find Maximum Removals From Source String
// https://leetcode.com/problems/find-maximum-removals-from-source-string/

class Solution {
    public int maxRemovals(String source, String pattern, int[] targetIndices) {
        int n = source.length();
        int lo = 0, hi = targetIndices.length;
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (ok(mid, source, pattern, targetIndices, n)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }

    private boolean ok(int removeFirst, String source, String pattern, int[] targetIndices, int n) {
        boolean[] mark = new boolean[n];
        for (int i = 0; i < removeFirst; i++) mark[targetIndices[i]] = true;
        int j = 0;
        for (int i = 0; i < n && j < pattern.length(); i++) {
            if (mark[i]) continue;
            if (source.charAt(i) == pattern.charAt(j)) j++;
        }
        return j == pattern.length();
    }
}
