// LeetCode 2550 - Count Collisions of Monkeys on a Polygon
// https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

int monkeyMove(int n) {
    const int MOD = 1000000007;
    long long a = 2, res = 1;
    int e = n;
    while (e > 0) {
        if (e & 1) res = res * a % MOD;
        a = a * a % MOD;
        e >>= 1;
    }
    return (int)((res - 2 + MOD) % MOD);
}
