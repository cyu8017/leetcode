// LeetCode 2513 - Minimize the Maximum of Two Arrays
// https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution {
    public int minimizeSet(int divisor1, int divisor2, int uniqueCnt1, int uniqueCnt2) {
        long lcm = 1L * divisor1 / gcd(divisor1, divisor2) * divisor2;
        boolean ok(long x) {
            long a = x - x / divisor1;
            long b = x - x / divisor2;
            long both = x - x / lcm;
            return a >= uniqueCnt1 && b >= uniqueCnt2 && both >= uniqueCnt1 + uniqueCnt2;
        }
        long lo = 1, hi = 1L << 62;
        while (lo < hi) {
            long mid = (lo + hi) / 2;
            if (Ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return (int)lo;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
