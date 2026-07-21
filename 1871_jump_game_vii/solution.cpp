// LeetCode 1871 - Jump Game VII
// https://leetcode.com/problems/jump-game-vii/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    bool canReach(std::string s, int minJump, int maxJump) {
        int n = static_cast<int>(s.size());
        std::vector<bool> reachable(n, false);
        reachable[0] = true;
        std::vector<int> prefix(n + 1, 0);
        for (int i = 0; i < n; i++) {
            if (i > 0 && s[i] == '0') {
                int left = std::max(0, i - maxJump);
                int right = i - minJump;
                if (right >= left && prefix[right + 1] - prefix[left] > 0) {
                    reachable[i] = true;
                }
            }
            prefix[i + 1] = prefix[i] + (reachable[i] ? 1 : 0);
        }
        return reachable[n - 1];
    }
};
