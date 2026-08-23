// LeetCode 2863 - Maximum Length of Semi-Decreasing Subarrays
// https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/

#include <vector>

class Solution {
public:
    int maxSubarrayLength(std::vector<int>& nums) {
        int n = (int)nums.size(), ans = 0;
        std::vector<int> st;
        for (int i = n - 1; i >= 0; i--) {
            if (st.empty() || nums[i] > nums[st.back()]) st.push_back(i);
        }
        for (int i = 0; i < n; i++) {
            while (!st.empty() && nums[i] > nums[st.back()]) {
                int j = st.back();
                st.pop_back();
                if (j - i + 1 > ans) ans = j - i + 1;
            }
        }
        return ans;
    }
};
