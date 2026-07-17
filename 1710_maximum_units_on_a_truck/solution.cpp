// LeetCode 1710 - Maximum Units on a Truck
// https://leetcode.com/problems/maximum-units-on-a-truck/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximumUnits(std::vector<std::vector<int>>& boxTypes, int truckSize) {
        std::sort(boxTypes.begin(), boxTypes.end(),
                  [](const std::vector<int>& a, const std::vector<int>& b) {
                      return a[1] > b[1];
                  });
        int total = 0;
        for (const auto& box : boxTypes) {
            int take = std::min(box[0], truckSize);
            total += take * box[1];
            truckSize -= take;
            if (truckSize == 0) {
                break;
            }
        }
        return total;
    }
};
