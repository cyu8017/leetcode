// LeetCode 3890 - Integers With Multiple Sum Of Two Cubes
// https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
    static inline std::vector<int> GOOD;
    static inline bool ready = false;

    static void init() {
        if (ready) return;
        const long long LIMIT = 1000000000LL;
        std::unordered_map<int, int> cnt;
        std::vector<long long> cubes(1001);
        for (int i = 0; i <= 1000; i++) cubes[i] = 1LL * i * i * i;
        for (int a = 1; a <= 1000; a++) {
            for (int b = a; b <= 1000; b++) {
                long long x = cubes[a] + cubes[b];
                if (x > LIMIT) break;
                cnt[(int)x]++;
            }
        }
        for (auto& [x, v] : cnt) {
            if (v > 1) GOOD.push_back(x);
        }
        std::sort(GOOD.begin(), GOOD.end());
        ready = true;
    }

public:
    std::vector<int> findGoodIntegers(int n) {
        init();
        auto it = std::upper_bound(GOOD.begin(), GOOD.end(), n);
        return std::vector<int>(GOOD.begin(), it);
    }
};
