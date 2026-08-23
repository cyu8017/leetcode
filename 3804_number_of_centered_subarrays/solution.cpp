// LeetCode 3804 - Number Of Centered Subarrays
// https://leetcode.com/problems/number-of-centered-subarrays/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int centeredSubarrays(std::vector<int>& nums) {
        int n = (int)nums.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            std::unordered_set<int> st;
            int s = 0;
            for (int j = i; j < n; j++) {
                s += nums[j];
                st.insert(nums[j]);
                if (st.count(s)) ans++;
            }
        }
        return ans;
    }
};
