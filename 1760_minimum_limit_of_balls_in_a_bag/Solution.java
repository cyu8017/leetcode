// LeetCode 1760 - Minimum Limit of Balls in a Bag
// https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

class Solution {
    public int minimumSize(int[] nums, int maxOperations) {
        int lo = 1;
        int hi = 0;
        for (int x : nums) {
            hi = Math.max(hi, x);
        }
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            long ops = 0;
            for (int x : nums) {
                ops += (x - 1) / mid;
            }
            if (ops <= maxOperations) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}
