// LeetCode 2550 - Count Collisions of Monkeys on a Polygon
// https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

class Solution {
    private static final int MOD = 1_000_000_007;

    public int monkeyMove(int n) {
        return (powMod(2, n) - 2 + MOD) % MOD;
    }

    private int powMod(long a, int e) {
        long res = 1;
        while (e > 0) {
            if ((e & 1) != 0) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return (int) res;
    }
}
