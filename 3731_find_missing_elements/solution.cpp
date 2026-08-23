// LeetCode 3731 - Find Missing Elements
// https://leetcode.com/problems/find-missing-elements/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<int> findMissingElements(std::vector<int>& nums) {
        int mn = 100, mx = 0;
        std::unordered_set<int> s;
        for (int x : nums) {
            mn = std::min(mn, x);
            mx = std::max(mx, x);
            s.insert(x);
        }
        std::vector<int> ans;
        for (int x = mn + 1; x < mx; x++) {
            if (!s.count(x)) ans.push_back(x);
        }
        return ans;
    }
};
