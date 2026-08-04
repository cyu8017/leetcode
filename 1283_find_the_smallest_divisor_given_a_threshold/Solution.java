// LeetCode 1283 - Find the Smallest Divisor Given a Threshold
// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution {
    public int smallestDivisor(int[] nums, int threshold) {
        int lo = 1, hi = 0;
        for (int x : nums) hi = Math.max(hi, x);
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            long sum = 0;
            for (int x : nums) sum += (x + mid - 1) / mid;
            if (sum <= threshold) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
