// LeetCode 3074 - Apple Redistribution into Boxes
// https://leetcode.com/problems/apple-redistribution-into-boxes/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minimumBoxes(std::vector<int>& apple, std::vector<int>& capacity) {
        std::sort(capacity.begin(), capacity.end());
        int s = 0;
        for (int x : apple) s += x;
        for (int i = 1; ; i++) {
            s -= capacity[(int)capacity.size() - i];
            if (s <= 0) return i;
        }
    }
};
