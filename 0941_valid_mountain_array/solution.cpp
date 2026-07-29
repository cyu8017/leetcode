// LeetCode 0941 - Valid Mountain Array
// https://leetcode.com/problems/valid-mountain-array/

#include <vector>

class Solution {
public:
    bool validMountainArray(std::vector<int>& arr) {
        int n = (int)arr.size();
        if (n < 3) return false;
        int i = 0;
        while (i + 1 < n && arr[i] < arr[i + 1]) i++;
        if (i == 0 || i == n - 1) return false;
        while (i + 1 < n && arr[i] > arr[i + 1]) i++;
        return i == n - 1;
    }
};
