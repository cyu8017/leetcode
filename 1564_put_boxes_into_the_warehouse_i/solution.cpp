// LeetCode 1564 - Put Boxes Into the Warehouse I
// https://leetcode.com/problems/put-boxes-into-the-warehouse-i/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxBoxesInWarehouse(std::vector<int>& boxes, std::vector<int>& warehouse) {
        for (std::size_t i = 1; i < warehouse.size(); ++i) {
            warehouse[i] = std::min(warehouse[i], warehouse[i - 1]);
        }
        std::sort(boxes.begin(), boxes.end());
        int room = static_cast<int>(warehouse.size()) - 1;
        int used = 0;
        for (int box : boxes) {
            while (room >= 0 && warehouse[room] < box) {
                --room;
            }
            if (room < 0) {
                break;
            }
            ++used;
            --room;
        }
        return used;
    }
};
