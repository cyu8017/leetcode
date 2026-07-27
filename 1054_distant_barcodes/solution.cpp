// LeetCode 1054 - Distant Barcodes
// https://leetcode.com/problems/distant-barcodes/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> rearrangeBarcodes(std::vector<int>& barcodes) {
        std::unordered_map<int, int> count;
        for (int x : barcodes) {
            ++count[x];
        }
        std::vector<std::pair<int, int>> items;
        items.reserve(count.size());
        for (const auto& [value, freq] : count) {
            items.push_back({freq, value});
        }
        std::sort(items.begin(), items.end(), std::greater<>());
        int n = static_cast<int>(barcodes.size());
        std::vector<int> ans(n);
        int i = 0;
        for (const auto& [freq, value] : items) {
            for (int k = 0; k < freq; ++k) {
                ans[i] = value;
                i += 2;
                if (i >= n) {
                    i = 1;
                }
            }
        }
        return ans;
    }
};
