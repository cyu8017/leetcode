#include <queue>
#include <set>
#include <tuple>
#include <vector>

class Solution {
public:
    int kthSmallest(std::vector<std::vector<int>>& mat, int k) {
        std::vector<int> sums{0};
        for (auto& row : mat) {
            using T = std::tuple<int, int, int>;
            std::priority_queue<T, std::vector<T>, std::greater<T>> heap;
            heap.push({sums[0] + row[0], 0, 0});
            std::vector<int> merged;
            std::set<std::pair<int,int>> seen{{0,0}};
            while (!heap.empty() && (int)merged.size() < k) {
                auto [value, i, j] = heap.top(); heap.pop();
                merged.push_back(value);
                if (j + 1 < (int)row.size() && !seen.count({i, j + 1})) {
                    seen.insert({i, j + 1});
                    heap.push({sums[i] + row[j + 1], i, j + 1});
                }
                if (j == 0 && i + 1 < (int)sums.size() && !seen.count({i + 1, 0})) {
                    seen.insert({i + 1, 0});
                    heap.push({sums[i + 1] + row[0], i + 1, 0});
                }
            }
            sums = std::move(merged);
        }
        return sums.back();
    }
};
