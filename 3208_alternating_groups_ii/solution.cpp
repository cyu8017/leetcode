// LeetCode 3208 - Alternating Groups II
// https://leetcode.com/problems/alternating-groups-ii/

#include <vector>

class Solution {
public:
    int numberOfAlternatingGroups(std::vector<int>& colors, int k) {
        int n = (int)colors.size(), cnt = 0, ans = 0;
        for (int i = 0; i < n * 2; i++) {
            if (i > 0 && colors[i % n] == colors[(i - 1) % n]) cnt = 1;
            else cnt++;
            if (i >= n && cnt >= k) ans++;
        }
        return ans;
    }
};
