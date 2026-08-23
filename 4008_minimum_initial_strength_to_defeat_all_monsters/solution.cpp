// LeetCode 4008 - Minimum Initial Strength to Defeat All Monsters
// https://leetcode.com/problems/minimum-initial-strength-to-defeat-all-monsters/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long minInitialStrength(std::vector<int>& monsters, std::vector<std::vector<int>>& boosts) {
        int n = (int)monsters.size();
        std::vector<int64_t> d(n + 1, 0);
        for (auto& b : boosts) {
            d[b[0]] += (int64_t)b[2];
            d[b[1] + 1] -= (int64_t)b[2];
        }

        auto check = [&](int64_t v) -> bool {
            int64_t bonus = 0;
            for (int i = 0; i < n; i++) {
                bonus += d[i];
                if (v + bonus < (int64_t)monsters[i]) return false;
                v -= (int64_t)monsters[i];
                if (v < 0) v = 0;
            }
            return true;
        };

        int64_t left = 0, right = 1000000000000000LL;
        while (left < right) {
            int64_t mid = (left + right) / 2;
            if (check(mid)) right = mid;
            else left = mid + 1;
        }
        return left;
    }
};
