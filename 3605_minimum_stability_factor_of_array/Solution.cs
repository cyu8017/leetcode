// LeetCode 3605 - Minimum Stability Factor of Array
// https://leetcode.com/problems/minimum-stability-factor-of-array/

public class Solution {
    static int Gcd(int a, int b) {
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }
    public int MinStable(int[] nums, int maxC) {
        int n = nums.Length;
        bool Ok(int x) {
            if (x >= n) return true;
            int changes = 0, i = 0;
            while (i + x < n) {
                int g = nums[i];
                for (int j = i + 1; j <= i + x; j++) g = Gcd(g, nums[j]);
                if (g > 1) {
                    changes++;
                    i += x + 1;
                } else {
                    i++;
                }
            }
            return changes <= maxC;
        }
        int lo = 0, hi = n;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (Ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
