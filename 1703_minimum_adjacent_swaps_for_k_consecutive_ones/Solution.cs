// LeetCode 1703 - Minimum Adjacent Swaps for K Consecutive Ones
// https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/

public class Solution {
    public int MinMoves(int[] nums, int k) {
        var adjusted = new List<long>();
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == 1) {
                adjusted.Add(i - adjusted.Count);
            }
        }
        int m = adjusted.Count;
        var prefix = new long[m + 1];
        for (int i = 0; i < m; i++) {
            prefix[i + 1] = prefix[i] + adjusted[i];
        }
        long best = long.MaxValue;
        for (int left = 0; left + k <= m; left++) {
            int right = left + k;
            int mid = left + k / 2;
            long median = adjusted[mid];
            long cost = median * (mid - left) - (prefix[mid] - prefix[left]);
            cost += (prefix[right] - prefix[mid + 1]) - median * (right - mid - 1);
            best = Math.Min(best, cost);
        }
        return (int)best;
    }
}
