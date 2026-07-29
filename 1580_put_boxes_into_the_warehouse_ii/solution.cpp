// LeetCode 1580 - Put Boxes Into the Warehouse II
// https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxBoxesInWarehouse(std::vector<int>& boxes, std::vector<int>& warehouse) {
        const int n = static_cast<int>(warehouse.size());
        std::vector<int> left = warehouse;
        std::vector<int> right = warehouse;
        for (int i = 1; i < n; ++i) {
            left[i] = std::min(left[i], left[i - 1]);
        }
        for (int i = n - 2; i >= 0; --i) {
            right[i] = std::min(right[i], right[i + 1]);
        }
        std::vector<int> capacity(n);
        for (int i = 0; i < n; ++i) {
            capacity[i] = std::max(left[i], right[i]);
        }
        std::sort(capacity.begin(), capacity.end());
        std::sort(boxes.begin(), boxes.end());
        int i = 0;
        for (int room : capacity) {
            if (i < static_cast<int>(boxes.size()) && boxes[i] <= room) {
                ++i;
            }
        }
        return i;
    }
};
