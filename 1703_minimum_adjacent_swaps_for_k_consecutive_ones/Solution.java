// LeetCode 1703 - Minimum Adjacent Swaps for K Consecutive Ones
// https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/

class Solution {
    public int minMoves(int[] nums, int k) {
        int onesCount = 0;
        for (int num : nums) {
            if (num == 1) {
                onesCount++;
            }
        }
        long[] adjusted = new long[onesCount];
        int idx = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                adjusted[idx] = i - idx;
                idx++;
            }
        }
        long[] prefix = new long[onesCount + 1];
        for (int i = 0; i < onesCount; i++) {
            prefix[i + 1] = prefix[i] + adjusted[i];
        }
        long best = Long.MAX_VALUE;
        for (int left = 0; left + k <= onesCount; left++) {
            int right = left + k;
            int mid = left + k / 2;
            long median = adjusted[mid];
            long cost = median * (mid - left) - (prefix[mid] - prefix[left]);
            cost += (prefix[right] - prefix[mid + 1]) - median * (right - mid - 1);
            best = Math.min(best, cost);
        }
        return (int) best;
    }
}
