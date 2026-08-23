// LeetCode 3594 - Minimum Time to Transport All Individuals
// https://leetcode.com/problems/minimum-time-to-transport-all-individuals/

#include <algorithm>
#include <vector>

class Solution {
public:
    double minTime(int n, int k, int m, std::vector<int>& time, std::vector<double>& mul) {
        std::vector<int> t = time;
        std::sort(t.begin(), t.end());
        double total = 0;
        int stage = 0, left = n;
        while (left > 0) {
            int take = std::min(k, left);
            int slow = t[left - 1];
            total += (double)slow * mul[stage % m];
            left -= take;
            stage++;
            if (left > 0) {
                total += (double)t[0] * mul[stage % m];
                stage++;
            }
        }
        return total;
    }
};
