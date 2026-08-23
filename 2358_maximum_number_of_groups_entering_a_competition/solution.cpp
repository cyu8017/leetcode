// LeetCode 2358 - Maximum Number of Groups Entering a Competition
// https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

#include <vector>

class Solution {
public:
    int maximumGroups(std::vector<int>& grades) {
        int n = (int)grades.size();
        int k = 0;
        while ((k + 1LL) * (k + 2) / 2 <= n) k++;
        return k;
    }
};
