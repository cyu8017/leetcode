// LeetCode 1923 - Longest Common Subpath
#include <algorithm>
#include <set>
#include <unordered_set>
#include <vector>

class Solution {
    static constexpr long long BASE1 = 911382323, MOD1 = 1000000007;
    static constexpr long long BASE2 = 972663749, MOD2 = 1000000009;
    long long modPow(long long a, long long e, long long mod) {
        long long r = 1;
        while (e) {
            if (e & 1) r = r * a % mod;
            a = a * a % mod;
            e >>= 1;
        }
        return r;
    }
public:
    int longestCommonSubpath(int n, std::vector<std::vector<int>>& paths) {
        (void)n;
        auto hasCommon = [&](int length) {
            if (length == 0) return true;
            std::set<std::pair<long long, long long>>* common = nullptr;
            std::set<std::pair<long long, long long>> commonOwned;
            long long pow1 = modPow(BASE1, length, MOD1);
            long long pow2 = modPow(BASE2, length, MOD2);
            for (auto& path : paths) {
                if ((int)path.size() < length) return false;
                long long h1 = 0, h2 = 0;
                std::set<std::pair<long long, long long>> seen;
                for (int i = 0; i < (int)path.size(); i++) {
                    h1 = (h1 * BASE1 + path[i] + 1) % MOD1;
                    h2 = (h2 * BASE2 + path[i] + 1) % MOD2;
                    if (i >= length) {
                        h1 = (h1 - (path[i - length] + 1) * pow1 % MOD1 + MOD1) % MOD1;
                        h2 = (h2 - (path[i - length] + 1) * pow2 % MOD2 + MOD2) % MOD2;
                    }
                    if (i >= length - 1) seen.insert({h1, h2});
                }
                if (!common) {
                    commonOwned = std::move(seen);
                    common = &commonOwned;
                } else {
                    std::set<std::pair<long long, long long>> nxt;
                    for (auto& p : *common) if (seen.count(p)) nxt.insert(p);
                    commonOwned.swap(nxt);
                    if (commonOwned.empty()) return false;
                }
            }
            return true;
        };
        int lo = 0, hi = (int)paths[0].size();
        for (auto& p : paths) hi = std::min(hi, (int)p.size());
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (hasCommon(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};
