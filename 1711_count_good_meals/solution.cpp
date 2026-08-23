// LeetCode 1711 - Count Good Meals
// https://leetcode.com/problems/count-good-meals/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int countPairs(std::vector<int>& deliciousness) {
        const long long mod = 1000000007LL;
        std::unordered_map<int, long long> seen;
        long long ans = 0;
        for (int value : deliciousness) {
            for (int power = 0; power < 22; power++) {
                auto it = seen.find((1 << power) - value);
                if (it != seen.end()) {
                    ans += it->second;
                }
            }
            seen[value]++;
        }
        return static_cast<int>(ans % mod);
    }
};
