// LeetCode 3824 - Minimum K To Reduce Array Within Limit
// https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/

public class Solution {
    public int MinimumK(int[] nums) {
        bool Check(int k) {
            long t = 0;
            foreach (int x in nums) t += (x + k - 1) / k;
            return t <= 1L * k * k;
        }
        int lo = 1, hi = 100000;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (Check(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
