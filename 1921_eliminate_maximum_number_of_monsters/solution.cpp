// LeetCode 1921 - Eliminate Maximum Number of Monsters
// https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

#include <algorithm>
#include <vector>

class Solution {
public:
    int eliminateMaximum(std::vector<int>& dist, std::vector<int>& speed) {
        int n = (int)dist.size();
        std::vector<int> arrival(n);
        for (int i = 0; i < n; i++) arrival[i] = (dist[i] + speed[i] - 1) / speed[i];
        std::sort(arrival.begin(), arrival.end());
        for (int i = 0; i < n; i++) {
            if (arrival[i] <= i) return i;
        }
        return n;
    }
};
