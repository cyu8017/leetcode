// LeetCode 3009 - Maximum Number of Intersections on the Chart
// https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/

#include <map>
#include <vector>

class Solution {
public:
    int maxIntersectionCount(std::vector<int>& y) {
        int n = (int)y.size();
        std::map<int, int> line;
        for (int i = 1; i < n; i++) {
            int start = 2 * y[i - 1];
            int end = 2 * y[i];
            if (i != n - 1) {
                if (y[i] > y[i - 1]) end--;
                else end++;
            }
            int a = start, b = end;
            if (a > b) std::swap(a, b);
            line[a]++;
            line[b + 1]--;
        }
        int ans = 0, cur = 0;
        for (auto& kv : line) {
            cur += kv.second;
            if (cur > ans) ans = cur;
        }
        return ans;
    }
};
