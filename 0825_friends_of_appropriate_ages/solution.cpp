// LeetCode 0825 - Friends Of Appropriate Ages
// https://leetcode.com/problems/friends-of-appropriate-ages/

#include <vector>

class Solution {
public:
    int numFriendRequests(std::vector<int>& ages) {
        std::vector<int> count(121, 0);
        for (int age : ages) {
            ++count[age];
        }
        int ans = 0;
        for (int x = 1; x <= 120; ++x) {
            if (count[x] == 0) {
                continue;
            }
            for (int y = 1; y <= 120; ++y) {
                if (count[y] == 0) {
                    continue;
                }
                if (y <= 0.5 * x + 7 || y > x || (y > 100 && x < 100)) {
                    continue;
                }
                ans += count[x] * count[y];
                if (x == y) {
                    ans -= count[x];
                }
            }
        }
        return ans;
    }
};
