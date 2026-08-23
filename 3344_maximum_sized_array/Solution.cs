// LeetCode 3344 - Maximum Sized Array
// https://leetcode.com/problems/maximum-sized-array/

public class Solution {
    public int MaxSizedArray(long s) {
        bool Ok(long n) {
            long sum = 0;
            for (long i = 0; i < n; i++) {
                for (long j = 0; j < n; j++) {
                    long ij = i | j;
                    sum += ij * (n - 1) * n / 2;
                    if (sum > s) return false;
                }
            }
            return sum <= s;
        }
        long lo = 1, hi = 2000;
        while (lo < hi) {
            long mid = (lo + hi + 1) / 2;
            if (Ok(mid)) lo = mid;
            else hi = mid - 1;
        }
        return (int)lo;
    }
}
