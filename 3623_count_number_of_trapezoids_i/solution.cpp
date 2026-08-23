// LeetCode 3623 - Count Number of Trapezoids I
// https://leetcode.com/problems/count-number-of-trapezoids-i/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int countTrapezoids(std::vector<std::vector<int>>& points) {
        const int mod = 1000000007;
        std::unordered_map<int, int> cnt;
        for (auto& p : points) cnt[p[1]]++;
        long long ans = 0, s = 0;
        for (auto& [_, v] : cnt) {
            long long t = 1LL * v * (v - 1) / 2;
            ans = (ans + s * t) % mod;
            s += t;
        }
        return (int)ans;
    }
};
