// LeetCode 1539 - Kth Missing Positive Number
// https://leetcode.com/problems/kth-missing-positive-number/

#include <vector>

class Solution {
public:
    int findKthPositive(std::vector<int>& arr, int k) {
        int left = 0;
        int right = static_cast<int>(arr.size());
        while (left < right) {
            int middle = (left + right) / 2;
            if (arr[middle] - middle - 1 < k) {
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        return left + k;
    }
};
