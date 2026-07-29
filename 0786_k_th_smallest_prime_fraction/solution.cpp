// LeetCode 0786 - K-th Smallest Prime Fraction
// https://leetcode.com/problems/k-th-smallest-prime-fraction/

#include <queue>
#include <tuple>
#include <vector>

class Solution {
public:
    std::vector<int> kthSmallestPrimeFraction(std::vector<int>& arr, int k) {
        int n = static_cast<int>(arr.size());
        using Item = std::tuple<double, int, int>;
        std::priority_queue<Item, std::vector<Item>, std::greater<Item>> heap;
        for (int i = 0; i < n - 1; ++i) {
            heap.push({static_cast<double>(arr[i]) / arr[n - 1], i, n - 1});
        }
        for (int t = 0; t < k - 1; ++t) {
            auto [_, i, j] = heap.top();
            heap.pop();
            if (j - 1 > i) {
                heap.push({static_cast<double>(arr[i]) / arr[j - 1], i, j - 1});
            }
        }
        auto [_, i, j] = heap.top();
        return {arr[i], arr[j]};
    }
};
