// LeetCode 1053 - Previous Permutation With One Swap
// https://leetcode.com/problems/previous-permutation-with-one-swap/

#include <vector>

class Solution {
public:
    std::vector<int> prevPermOpt1(std::vector<int>& arr) {
        int n = static_cast<int>(arr.size());
        int i = n - 2;
        while (i >= 0 && arr[i] <= arr[i + 1]) {
            --i;
        }
        if (i < 0) {
            return arr;
        }
        int j = n - 1;
        while (arr[j] >= arr[i] || arr[j] == arr[j - 1]) {
            --j;
        }
        std::swap(arr[i], arr[j]);
        return arr;
    }
};
