// LeetCode 1287 - Element Appearing More Than 25% In Sorted Array
// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

#include <algorithm>
#include <vector>

class Solution {
public:
    int findSpecialInteger(std::vector<int>& arr) {
        const int n = static_cast<int>(arr.size());
        for (int value : {arr[n / 4], arr[n / 2], arr[3 * n / 4]}) {
            if (std::count(arr.begin(), arr.end(), value) > n / 4) {
                return value;
            }
        }
        return arr[0];
    }
};
