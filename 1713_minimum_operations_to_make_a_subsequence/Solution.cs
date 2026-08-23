// LeetCode 1713 - Minimum Operations to Make a Subsequence
// https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/

public class Solution {
    public int MinOperations(int[] target, int[] arr) {
        var pos = new Dictionary<int, int>();
        for (int i = 0; i < target.Length; i++) {
            pos[target[i]] = i;
        }
        var lis = new List<int>();
        foreach (int value in arr) {
            if (!pos.TryGetValue(value, out int idx)) {
                continue;
            }
            int lo = 0;
            int hi = lis.Count;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (lis[mid] < idx) {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            if (lo == lis.Count) {
                lis.Add(idx);
            } else {
                lis[lo] = idx;
            }
        }
        return target.Length - lis.Count;
    }
}
