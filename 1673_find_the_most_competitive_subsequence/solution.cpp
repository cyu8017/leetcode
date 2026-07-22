// LeetCode 1673 - Find the Most Competitive Subsequence
// https://leetcode.com/problems/find-the-most-competitive-subsequence/

#include <vector>

class Solution {
public:
    std::vector<int> mostCompetitive(std::vector<int>& nums, int k) {
        std::vector<int> st;
        int n = static_cast<int>(nums.size());
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && st.back() > nums[i] &&
                   static_cast<int>(st.size()) - 1 + n - i >= k) {
                st.pop_back();
            }
            if (static_cast<int>(st.size()) < k) {
                st.push_back(nums[i]);
            }
        }
        return st;
    }
};
