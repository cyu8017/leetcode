// LeetCode 0849 - Maximize Distance to Closest Person
// https://leetcode.com/problems/maximize-distance-to-closest-person/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxDistToClosest(std::vector<int>& seats) {
        int n = static_cast<int>(seats.size());
        int prev = -1, ans = 0;
        for (int i = 0; i < n; ++i) {
            if (seats[i]) {
                if (prev == -1) {
                    ans = i;
                } else {
                    ans = std::max(ans, (i - prev) / 2);
                }
                prev = i;
            }
        }
        ans = std::max(ans, n - 1 - prev);
        return ans;
    }
};
