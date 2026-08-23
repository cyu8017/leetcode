// LeetCode 0835 - Image Overlap
// https://leetcode.com/problems/image-overlap/

#include <algorithm>
#include <unordered_map>
#include <utility>
#include <vector>

class Solution {
public:
    int largestOverlap(std::vector<std::vector<int>>& img1,
                       std::vector<std::vector<int>>& img2) {
        int n = static_cast<int>(img1.size());
        std::vector<std::pair<int, int>> ones1, ones2;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (img1[i][j]) {
                    ones1.emplace_back(i, j);
                }
                if (img2[i][j]) {
                    ones2.emplace_back(i, j);
                }
            }
        }
        if (ones1.empty() || ones2.empty()) {
            return 0;
        }
        std::unordered_map<long long, int> shifts;
        int best = 0;
        for (auto [x1, y1] : ones1) {
            for (auto [x2, y2] : ones2) {
                long long key = (static_cast<long long>(x1 - x2 + n) << 16) |
                                (y1 - y2 + n);
                best = std::max(best, ++shifts[key]);
            }
        }
        return best;
    }
};
