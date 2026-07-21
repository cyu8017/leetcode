// LeetCode 1820 - Maximum Number of Accepted Invitations
// https://leetcode.com/problems/maximum-number-of-accepted-invitations/

#include <functional>
#include <vector>

class Solution {
public:
    int maximumInvitations(std::vector<std::vector<int>>& grid) {
        int boys = static_cast<int>(grid.size());
        int girls = static_cast<int>(grid[0].size());
        std::vector<int> matchGirl(girls, -1);

        std::function<bool(int, std::vector<char>&)> dfs = [&](int boy, std::vector<char>& seen) -> bool {
            for (int girl = 0; girl < girls; ++girl) {
                if (grid[boy][girl] && !seen[girl]) {
                    seen[girl] = 1;
                    if (matchGirl[girl] == -1 || dfs(matchGirl[girl], seen)) {
                        matchGirl[girl] = boy;
                        return true;
                    }
                }
            }
            return false;
        };

        int ans = 0;
        for (int boy = 0; boy < boys; ++boy) {
            std::vector<char> seen(girls, 0);
            if (dfs(boy, seen)) {
                ++ans;
            }
        }
        return ans;
    }
};
