// LeetCode 3916 - Number of ZigZag Arrays III
// https://leetcode.com/problems/number-of-zigzag-arrays-iii/

#include <vector>

class Solution {
public:
    int zigZagArrays(int n, int l, int r) {
        const long long mod = 1000000007;
        int points = n + 1;
        std::vector<long long> values(points + 1, 0);
        for (int m = 1; m <= points; m++) {
            std::vector<long long> up(m), down(m);
            for (int value = 0; value < m; value++) {
                up[value] = value;
                down[value] = m - 1 - value;
            }
            for (int length = 3; length <= n; length++) {
                std::vector<long long> nextUp(m), nextDown(m);
                long long prefix = 0;
                for (int value = 0; value < m; value++) {
                    nextUp[value] = prefix;
                    prefix = (prefix + down[value]) % mod;
                }
                long long suffix = 0;
                for (int value = m - 1; value >= 0; value--) {
                    nextDown[value] = suffix;
                    suffix = (suffix + up[value]) % mod;
                }
                up.swap(nextUp);
                down.swap(nextDown);
            }
            for (int value = 0; value < m; value++) {
                values[m] = (values[m] + up[value] + down[value]) % mod;
            }
        }
        long long x = (r - l + 1) % mod;
        if (r - l + 1 <= points) return (int)values[r - l + 1];
        std::vector<long long> prefix(points + 2), suffix(points + 2);
        prefix[0] = 1;
        for (int i = 1; i <= points; i++) {
            prefix[i] = prefix[i - 1] * ((x - i + mod) % mod) % mod;
        }
        suffix[points + 1] = 1;
        for (int i = points; i >= 1; i--) {
            suffix[i] = suffix[i + 1] * ((x - i + mod) % mod) % mod;
        }
        std::vector<long long> factorial(points + 1);
        factorial[0] = 1;
        for (int i = 1; i <= points; i++) factorial[i] = factorial[i - 1] * i % mod;
        auto powm = [&](long long a, long long e) {
            long long res = 1;
            while (e > 0) {
                if (e & 1) res = res * a % mod;
                a = a * a % mod;
                e >>= 1;
            }
            return res;
        };
        long long answer = 0;
        for (int i = 1; i <= points; i++) {
            long long numerator = prefix[i - 1] * suffix[i + 1] % mod;
            long long denominator = factorial[i - 1] * factorial[points - i] % mod;
            long long term = values[i] * numerator % mod * powm(denominator, mod - 2) % mod;
            if ((points - i) % 2 == 1) answer -= term;
            else answer += term;
            answer %= mod;
        }
        if (answer < 0) answer += mod;
        return (int)answer;
    }
};
