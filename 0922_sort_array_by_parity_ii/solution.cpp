// LeetCode 0922 - Sort Array By Parity II
// https://leetcode.com/problems/sort-array-by-parity-ii/

#include <vector>

class Solution {
public:
    std::vector<int> sortArrayByParityII(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> ans(n);
        int even = 0, odd = 1;
        for (int x : nums) {
            if (x % 2 == 0) {
                ans[even] = x;
                even += 2;
            } else {
                ans[odd] = x;
                odd += 2;
            }
        }
        return ans;
    }
};
