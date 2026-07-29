#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int distinctEchoSubstrings(std::string text) {
        int n = (int)text.size();
        const long long mod1 = 1000000007, mod2 = 1000000009, base = 911382323;
        std::vector<long long> h1(n + 1), h2(n + 1), p1(n + 1, 1), p2(n + 1, 1);
        for (int i = 0; i < n; ++i) {
            int code = text[i];
            h1[i + 1] = (h1[i] * base + code) % mod1;
            h2[i + 1] = (h2[i] * base + code) % mod2;
            p1[i + 1] = p1[i] * base % mod1;
            p2[i + 1] = p2[i] * base % mod2;
        }
        auto hashed = [&](int left, int right) {
            int length = right - left;
            long long a = (h1[right] - h1[left] * p1[length] % mod1 + mod1) % mod1;
            long long b = (h2[right] - h2[left] * p2[length] % mod2 + mod2) % mod2;
            return std::pair{a, b};
        };
        std::unordered_set<unsigned long long> echoes;
        for (int half = 1; half <= n / 2; ++half) {
            for (int left = 0; left + 2 * half <= n; ++left) {
                if (hashed(left, left + half) == hashed(left + half, left + 2 * half)) {
                    auto [a, b] = hashed(left, left + 2 * half);
                    echoes.insert(((unsigned long long)(2 * half) << 48) ^ ((unsigned long long)a << 24) ^ (unsigned long long)b);
                }
            }
        }
        return (int)echoes.size();
    }
};
