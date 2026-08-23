// LeetCode 3871 - Count Commas In Range Ii
// https://leetcode.com/problems/count-commas-in-range-ii/

public class Solution {
    public long CountCommas(long n) {
        long ans = 0;
        for (long x = 1000; x <= n; x *= 1000) ans += n - x + 1;
        return ans;
    }
}
