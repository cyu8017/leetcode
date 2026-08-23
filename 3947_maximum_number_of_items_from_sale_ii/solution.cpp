// LeetCode 3947 - Maximum Number of Items From Sale II
// https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxItems(std::vector<std::vector<int>>& items, int budget) {
        int n = (int)items.size();
        std::vector<int> frequency(n + 1, 0);
        int minimumPrice = items[0][1];
        for (auto& item : items) {
            frequency[item[0]]++;
            minimumPrice = std::min(minimumPrice, item[1]);
        }
        struct Batch { int price, count; };
        std::vector<Batch> batches;
        for (auto& item : items) {
            int gain = 0;
            for (int multiple = item[0]; multiple <= n; multiple += item[0]) gain += frequency[multiple];
            gain--;
            if (gain > 0 && item[1] < 2 * minimumPrice) batches.push_back({item[1], gain});
        }
        std::sort(batches.begin(), batches.end(), [](const Batch& a, const Batch& b) {
            return a.price < b.price;
        });
        long long remaining = budget;
        long long answer = budget / minimumPrice;
        long long boosted = 0;
        for (auto& current : batches) {
            long long count = current.count;
            long long affordable = remaining / current.price;
            if (affordable < count) count = affordable;
            remaining -= count * current.price;
            boosted += count;
            long long total = 2 * boosted + remaining / minimumPrice;
            if (total > answer) answer = total;
            if (count < current.count) break;
        }
        return (int)answer;
    }
};
