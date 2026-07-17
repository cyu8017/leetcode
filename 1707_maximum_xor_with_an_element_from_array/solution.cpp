// LeetCode 1707 - Maximum XOR With an Element From Array
// https://leetcode.com/problems/maximum-xor-with-an-element-from-array/

#include <algorithm>
#include <array>
#include <numeric>
#include <vector>

class Solution {
public:
    std::vector<int> maximizeXor(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        std::sort(nums.begin(), nums.end());
        std::vector<int> order(queries.size());
        std::iota(order.begin(), order.end(), 0);
        std::sort(order.begin(), order.end(), [&](int a, int b) {
            return queries[a][1] < queries[b][1];
        });

        std::vector<std::array<int, 2>> children;
        children.push_back({-1, -1});

        auto insert = [&](int num) {
            int node = 0;
            for (int bit = 31; bit >= 0; bit--) {
                int b = (num >> bit) & 1;
                if (children[node][b] == -1) {
                    children[node][b] = static_cast<int>(children.size());
                    children.push_back({-1, -1});
                }
                node = children[node][b];
            }
        };

        std::vector<int> ans(queries.size(), -1);
        size_t added = 0;
        for (int qi : order) {
            int x = queries[qi][0];
            int limit = queries[qi][1];
            while (added < nums.size() && nums[added] <= limit) {
                insert(nums[added]);
                added++;
            }
            if (added == 0) {
                continue;
            }
            int node = 0;
            int value = 0;
            for (int bit = 31; bit >= 0; bit--) {
                int b = (x >> bit) & 1;
                int want = b ^ 1;
                if (children[node][want] != -1) {
                    value |= 1 << bit;
                    node = children[node][want];
                } else {
                    node = children[node][b];
                }
            }
            ans[qi] = value;
        }
        return ans;
    }
};
