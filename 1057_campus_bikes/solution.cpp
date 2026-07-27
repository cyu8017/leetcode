// LeetCode 1057 - Campus Bikes
// https://leetcode.com/problems/campus-bikes/

#include <algorithm>
#include <cstdlib>
#include <tuple>
#include <vector>

class Solution {
public:
    std::vector<int> assignBikes(std::vector<std::vector<int>>& workers,
                                 std::vector<std::vector<int>>& bikes) {
        std::vector<std::tuple<int, int, int>> triples;
        for (int w = 0; w < static_cast<int>(workers.size()); ++w) {
            for (int b = 0; b < static_cast<int>(bikes.size()); ++b) {
                int dist = std::abs(workers[w][0] - bikes[b][0]) +
                           std::abs(workers[w][1] - bikes[b][1]);
                triples.emplace_back(dist, w, b);
            }
        }
        std::sort(triples.begin(), triples.end());
        std::vector<int> ans(workers.size(), -1);
        std::vector<char> usedBikes(bikes.size(), 0);
        int assigned = 0;
        for (const auto& [dist, w, b] : triples) {
            (void)dist;
            if (ans[w] == -1 && !usedBikes[b]) {
                ans[w] = b;
                usedBikes[b] = 1;
                ++assigned;
                if (assigned == static_cast<int>(workers.size())) {
                    break;
                }
            }
        }
        return ans;
    }
};
