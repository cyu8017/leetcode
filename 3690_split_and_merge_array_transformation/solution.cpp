// LeetCode 3690 - Split and Merge Array Transformation
// https://leetcode.com/problems/split-and-merge-array-transformation/

#include <array>
#include <queue>
#include <unordered_set>
#include <vector>

class Solution {
    struct ArrHash {
        size_t operator()(const std::array<int, 6>& a) const {
            size_t h = 0;
            for (int x : a) h = h * 31 + (size_t)x;
            return h;
        }
    };

public:
    int minSplitMerge(std::vector<int>& nums1, std::vector<int>& nums2) {
        int n = (int)nums1.size();
        auto toArr = [&](const std::vector<int>& nums) {
            std::array<int, 6> t{};
            for (int i = 0; i < n; i++) t[i] = nums[i];
            return t;
        };
        auto start = toArr(nums1);
        auto target = toArr(nums2);
        std::unordered_set<std::array<int, 6>, ArrHash> vis{start};
        std::vector<std::array<int, 6>> q{start};
        for (int ans = 0;; ans++) {
            std::vector<std::array<int, 6>> nq;
            for (auto& cur : q) {
                if (cur == target) return ans;
                for (int l = 0; l < n; l++) {
                    for (int r = l; r < n; r++) {
                        std::vector<int> remain, sub;
                        for (int i = 0; i < l; i++) remain.push_back(cur[i]);
                        for (int i = r + 1; i < n; i++) remain.push_back(cur[i]);
                        for (int i = l; i <= r; i++) sub.push_back(cur[i]);
                        for (int pos = 0; pos <= (int)remain.size(); pos++) {
                            std::vector<int> nxtSlice;
                            nxtSlice.insert(nxtSlice.end(), remain.begin(), remain.begin() + pos);
                            nxtSlice.insert(nxtSlice.end(), sub.begin(), sub.end());
                            nxtSlice.insert(nxtSlice.end(), remain.begin() + pos, remain.end());
                            auto nxt = toArr(nxtSlice);
                            if (!vis.count(nxt)) {
                                vis.insert(nxt);
                                nq.push_back(nxt);
                            }
                        }
                    }
                }
            }
            q = std::move(nq);
        }
    }
};
