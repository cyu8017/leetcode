// LeetCode 1187 - Make Array Strictly Increasing
// https://leetcode.com/problems/make-array-strictly-increasing/

#include <algorithm>
#include <climits>
#include <map>
#include <vector>

class Solution {
public:
    int makeArrayIncreasing(std::vector<int>& arr1, std::vector<int>& arr2) {
        std::sort(arr2.begin(), arr2.end());
        arr2.erase(std::unique(arr2.begin(), arr2.end()), arr2.end());
        std::map<int, int> dp{{-1, 0}};
        for (int num : arr1) {
            std::map<int, int> neu;
            for (const auto& [prev, ops] : dp) {
                if (num > prev) {
                    auto it = neu.find(num);
                    if (it == neu.end() || ops < it->second) neu[num] = ops;
                }
                auto it2 = std::upper_bound(arr2.begin(), arr2.end(), prev);
                if (it2 != arr2.end()) {
                    int chosen = *it2;
                    auto it = neu.find(chosen);
                    if (it == neu.end() || ops + 1 < it->second) neu[chosen] = ops + 1;
                }
            }
            dp.swap(neu);
            if (dp.empty()) return -1;
        }
        int ans = INT_MAX;
        for (const auto& [_, ops] : dp) ans = std::min(ans, ops);
        return ans;
    }
};
