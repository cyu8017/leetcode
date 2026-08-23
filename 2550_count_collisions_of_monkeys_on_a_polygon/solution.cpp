// LeetCode 2550 - Count Collisions of Monkeys on a Polygon
// https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

class Solution {
public:
    int monkeyMove(int n) {
        const int MOD = 1000000007;
        auto powmod = [&](long long a, int e) {
            long long res = 1;
            while (e > 0) {
                if (e & 1) res = res * a % MOD;
                a = a * a % MOD;
                e >>= 1;
            }
            return (int)res;
        };
        return (powmod(2, n) - 2 + MOD) % MOD;
    }
};
