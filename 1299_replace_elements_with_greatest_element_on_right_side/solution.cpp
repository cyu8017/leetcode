// LeetCode 1299 - Replace Elements with Greatest Element on Right Side
// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> replaceElements(std::vector<int>& arr) {
        int greatest = -1;
        for (int i = static_cast<int>(arr.size()) - 1; i >= 0; --i) {
            int current = arr[i];
            arr[i] = greatest;
            greatest = std::max(greatest, current);
        }
        return arr;
    }
};
