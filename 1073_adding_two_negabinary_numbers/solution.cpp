// LeetCode 1073 - Adding Two Negabinary Numbers
// https://leetcode.com/problems/adding-two-negabinary-numbers/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> addNegabinary(std::vector<int>& arr1, std::vector<int>& arr2) {
        int i = static_cast<int>(arr1.size()) - 1;
        int j = static_cast<int>(arr2.size()) - 1;
        int carry = 0;
        std::vector<int> ans;
        while (i >= 0 || j >= 0 || carry) {
            int total = carry;
            if (i >= 0) {
                total += arr1[i--];
            }
            if (j >= 0) {
                total += arr2[j--];
            }
            ans.push_back(total & 1);
            carry = -(total >> 1);
        }
        while (ans.size() > 1 && ans.back() == 0) {
            ans.pop_back();
        }
        std::reverse(ans.begin(), ans.end());
        return ans;
    }
};
