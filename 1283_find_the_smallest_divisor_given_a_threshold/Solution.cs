// LeetCode 1283 - Find the Smallest Divisor Given a Threshold
// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

using System.Linq;

public class Solution {
    public int SmallestDivisor(int[] nums, int threshold) {
        int lo = 1, hi = nums.Max();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            long sum = 0;
            foreach (int x in nums) sum += (x + mid - 1) / mid;
            if (sum <= threshold) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
