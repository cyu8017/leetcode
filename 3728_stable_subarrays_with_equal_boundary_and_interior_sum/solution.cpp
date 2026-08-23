// LeetCode 3728 - Stable Subarrays With Equal Boundary and Interior Sum
// https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/

#include <unordered_map>
#include <utility>
#include <vector>

class Solution {
    struct KeyHash {
        size_t operator()(const std::pair<int, long long>& p) const {
            return std::hash<int>()(p.first) * 1000003ull + std::hash<long long>()(p.second);
        }
    };

public:
    long long countStableSubarrays(std::vector<int>& capacity) {
        int n = (int)capacity.size();
        std::vector<long long> s(n + 1);
        for (int i = 1; i <= n; i++) s[i] = s[i - 1] + capacity[i - 1];
        std::unordered_map<std::pair<int, long long>, int, KeyHash> cnt;
        long long ans = 0;
        for (int r = 2; r < n; r++) {
            int l = r - 2;
            cnt[{capacity[l], (long long)capacity[l] + s[l + 1]}]++;
            ans += cnt[{capacity[r], s[r]}];
        }
        return ans;
    }
};
