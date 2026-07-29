// LeetCode 1989 - Maximum Number of People That Can Be Caught in Tag
#include <cstdlib>
#include <vector>

class Solution {
public:
    int catchMaximumAmountofPeople(std::vector<int>& team, int dist) {
        int ans = 0, j = 0, n = (int)team.size();
        for (int i = 0; i < n; i++) {
            if (!team[i]) continue;
            while (j < n && (team[j] || i - j > dist)) j++;
            if (j < n && std::abs(i - j) <= dist) {
                ans++;
                j++;
            }
        }
        return ans;
    }
};
