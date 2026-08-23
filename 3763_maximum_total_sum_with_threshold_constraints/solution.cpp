// LeetCode 3763 - Maximum Total Sum With Threshold Constraints
// https://leetcode.com/problems/maximum-total-sum-with-threshold-constraints/

#include <algorithm>
#include <set>
#include <vector>

class Solution {
public:
    long long maxSum(std::vector<int>& nums, std::vector<int>& threshold) {
        int n = (int)nums.size();
        std::vector<int> idx(n);
        for (int i = 0; i < n; i++) idx[i] = i;
        std::sort(idx.begin(), idx.end(), [&](int a, int b) {
            return threshold[a] < threshold[b];
        });
        std::multiset<int> tree;
        long long ans = 0;
        int i = 0;
        for (int step = 1;; step++) {
            while (i < n && threshold[idx[i]] <= step) {
                tree.insert(nums[idx[i]]);
                i++;
            }
            if (tree.empty()) break;
            auto it = std::prev(tree.end());
            ans += *it;
            tree.erase(it);
        }
        return ans;
    }
};
