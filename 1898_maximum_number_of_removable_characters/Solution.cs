// LeetCode 1898 - Maximum Number of Removable Characters
// https://leetcode.com/problems/maximum-number-of-removable-characters/

public class Solution {
    public int MaximumRemovals(string s, string p, int[] removable) {
        bool StillSubsequence(int k) {
            var removed = new HashSet<int>();
            for (int i = 0; i < k; i++) {
                removed.Add(removable[i]);
            }
            int index = 0;
            for (int position = 0; position < s.Length; position++) {
                if (removed.Contains(position)) {
                    continue;
                }
                if (index < p.Length && s[position] == p[index]) {
                    index++;
                }
            }
            return index == p.Length;
        }

        int lo = 0;
        int hi = removable.Length;
        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            if (StillSubsequence(mid)) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }
}
