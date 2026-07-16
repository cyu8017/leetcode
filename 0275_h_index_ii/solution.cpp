// LeetCode 0275 - H-Index II
// https://leetcode.com/problems/h-index-ii/

#include <vector>

class Solution {
public:
    int hIndex(std::vector<int>& citations) {
        int left = 0;
        int right = static_cast<int>(citations.size()) - 1;
        int length = static_cast<int>(citations.size());
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int papers = length - mid;
            if (citations[mid] >= papers) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return length - left;
    }
};
