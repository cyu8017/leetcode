// LeetCode 3779 - Minimum Number Of Operations To Have Distinct Elements
// https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        std::unordered_set<int> st;
        for (int i = (int)nums.size() - 1; i >= 0; i--) {
            if (st.count(nums[i])) return i / 3 + 1;
            st.insert(nums[i]);
        }
        return 0;
    }
};
