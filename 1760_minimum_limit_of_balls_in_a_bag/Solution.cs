// LeetCode 1760 - Minimum Limit of Balls in a Bag
// https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

public class Solution {
    public int MinimumSize(int[] nums, int maxOperations) {
        int lo = 1;
        int hi = 0;
        foreach (int x in nums) {
            hi = System.Math.Max(hi, x);
        }
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            long ops = 0;
            foreach (int x in nums) {
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
