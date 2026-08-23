// LeetCode 3695 - Maximize Alternating Sum Using Swaps
// https://leetcode.com/problems/maximize-alternating-sum-using-swaps/

#include <algorithm>
#include <functional>
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long maxAlternatingSum(std::vector<int>& nums, std::vector<std::vector<int>>& swaps) {
        int n = (int)nums.size();
        std::vector<int> parent(n);
        for (int i = 0; i < n; i++) parent[i] = i;
        std::function<int(int)> find = [&](int x) -> int {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        };
        for (auto& s : swaps) {
            int a = find(s[0]), b = find(s[1]);
            if (a != b) parent[a] = b;
        }
        std::unordered_map<int, std::vector<int>> compVals, compIdx;
        for (int i = 0; i < n; i++) {
            int r = find(i);
            compVals[r].push_back(nums[i]);
            compIdx[r].push_back(i);
        }
        std::vector<int> arr(n);
        for (auto& [r, vals] : compVals) {
            auto& idxs = compIdx[r];
            std::sort(vals.begin(), vals.end(), std::greater<int>());
            std::vector<int> even, odd;
            for (int i : idxs) {
                if (i % 2 == 0) even.push_back(i);
                else odd.push_back(i);
            }
            std::sort(even.begin(), even.end());
            std::sort(odd.begin(), odd.end());
            int ei = 0;
            for (int v : vals) {
                if (ei < (int)even.size()) {
                    arr[even[ei]] = v;
                    ei++;
                } else {
                    arr[odd[ei - (int)even.size()]] = v;
                    ei++;
                }
            }
        }
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) ans += arr[i];
            else ans -= arr[i];
        }
        return ans;
    }
};
