// LeetCode 3861 - Minimum Capacity Box
// https://leetcode.com/problems/minimum-capacity-box/

#include <vector>

class Solution {
public:
    int minimumIndex(std::vector<int>& capacity, int itemSize) {
        int ans = -1;
        for (int i = 0; i < (int)capacity.size(); i++) {
            if (capacity[i] >= itemSize && (ans == -1 || capacity[i] < capacity[ans])) ans = i;
        }
        return ans;
    }
};
