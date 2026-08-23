// LeetCode 2832 - Maximal Range That Each Element Is Maximum in It
// https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/

#include <vector>

class Solution {
public:
    std::vector<int> maximumLength(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> left(n), right(n), st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && nums[st.back()] < nums[i]) st.pop_back();
            left[i] = st.empty() ? -1 : st.back();
            st.push_back(i);
        }
        st.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!st.empty() && nums[st.back()] <= nums[i]) st.pop_back();
            right[i] = st.empty() ? n : st.back();
            st.push_back(i);
        }
        std::vector<int> ans(n);
        for (int i = 0; i < n; i++) ans[i] = right[i] - left[i] - 1;
        return ans;
    }
};
