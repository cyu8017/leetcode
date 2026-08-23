// LeetCode 2550 - Count Collisions of Monkeys on a Polygon
// https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

public class Solution {
    public int MonkeyMove(int n) {
        const int MOD = 1000000007;
        int PowMod(long a, int e) {
            long res = 1;
            while (e > 0) {
                if ((e & 1) != 0) res = res * a % MOD;
                a = a * a % MOD;
                e >>= 1;
            }
            return (int)res;
        }
        return (PowMod(2, n) - 2 + MOD) % MOD;
    }
}
