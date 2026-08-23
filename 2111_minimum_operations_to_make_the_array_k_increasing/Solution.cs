// LeetCode 2111 - Minimum Operations to Make the Array K-Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/

public class Solution {
    public int KIncreasing(int[] arr, int k) {
        int ans = 0, n = arr.Length;
        for (int start = 0; start < k; start++) {
            var seq = new List<int>();
            for (int i = start; i < n; i += k) seq.Add(arr[i]);
            var tails = new List<int>();
            foreach (int x in seq) {
                int lo = 0, hi = tails.Count;
                while (lo < hi) {
                    int mid = (lo + hi) / 2;
                    if (tails[mid] <= x) lo = mid + 1;
                    else hi = mid;
                }
                if (lo == tails.Count) tails.Add(x);
                else tails[lo] = x;
            }
            ans += seq.Count - tails.Count;
        }
        return ans;
    }
}
