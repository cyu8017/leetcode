// LeetCode 1574 - Shortest Subarray to be Removed to Make Array Sorted
// https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

#include <algorithm>
#include <vector>

class Solution {
public:
    int findLengthOfShortestSubarray(std::vector<int>& arr) {
        const int n = static_cast<int>(arr.size());
        int right = n - 1;
        while (right > 0 && arr[right - 1] <= arr[right]) {
            --right;
        }
        if (right == 0) {
            return 0;
        }
        int answer = right;
        int left = 0;
        while (left == 0 || (left < n && arr[left - 1] <= arr[left])) {
            while (right < n && arr[right] < arr[left]) {
                ++right;
            }
            answer = std::min(answer, right - left - 1);
            ++left;
            if (left >= n) {
                break;
            }
        }
        return answer;
    }
};
