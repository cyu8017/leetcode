// LeetCode 3510 - Minimum Pair Removal to Sort Array II
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/

#include <vector>
#include <set>

class Solution {
public:
    int minimumPairRemoval(std::vector<int>& nums) {
        int n = (int)nums.size();
        int inv = 0, ans = 0;
        std::set<std::pair<int, int>> sl;
        std::set<int> idx;
        for (int i = 0; i < n; i++) idx.insert(i);
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] > nums[i + 1]) inv++;
            sl.insert({nums[i] + nums[i + 1], i});
        }
        while (inv > 0) {
            ans++;
            auto p = *sl.begin();
            sl.erase(sl.begin());
            int s = p.first, i = p.second;
            auto jIt = idx.lower_bound(i + 1);
            int j = *jIt;
            if (nums[i] > nums[j]) inv--;
            auto hIt = idx.upper_bound(i - 1);
            if (hIt != idx.begin()) {
                --hIt;
                int h = *hIt;
                if (nums[h] > nums[i]) inv--;
                sl.erase({nums[h] + nums[i], h});
                if (nums[h] > s) inv++;
                sl.insert({nums[h] + s, h});
            }
            auto kIt = idx.lower_bound(j + 1);
            if (kIt != idx.end()) {
                int k = *kIt;
                if (nums[j] > nums[k]) inv--;
                sl.erase({nums[j] + nums[k], j});
                if (s > nums[k]) inv++;
                sl.insert({s + nums[k], i});
            }
            nums[i] = s;
            idx.erase(j);
        }
        return ans;
    }
};
