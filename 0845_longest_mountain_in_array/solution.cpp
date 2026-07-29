// LeetCode 0845 - Longest Mountain in Array
// https://leetcode.com/problems/longest-mountain-in-array/

#include <algorithm>
#include <vector>

class Solution {
public:
    int longestMountain(std::vector<int>& arr) {
        int n = static_cast<int>(arr.size());
        int ans = 0, i = 0;
        while (i < n) {
            int j = i;
            if (j + 1 < n && arr[j] < arr[j + 1]) {
                while (j + 1 < n && arr[j] < arr[j + 1]) {
                    ++j;
                }
                if (j + 1 < n && arr[j] > arr[j + 1]) {
                    while (j + 1 < n && arr[j] > arr[j + 1]) {
                        ++j;
                    }
                    ans = std::max(ans, j - i + 1);
                    i = j;
                    continue;
                }
            }
            ++i;
        }
        return ans;
    }
};
