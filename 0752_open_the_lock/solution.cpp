// LeetCode 0752 - Open the Lock
// https://leetcode.com/problems/open-the-lock/

#include <queue>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int openLock(std::vector<std::string>& deadends, std::string target) {
        std::unordered_set<std::string> dead(deadends.begin(), deadends.end());
        if (dead.count("0000")) {
            return -1;
        }
        std::queue<std::pair<std::string, int>> q;
        std::unordered_set<std::string> seen{"0000"};
        q.push({"0000", 0});
        while (!q.empty()) {
            auto [state, steps] = q.front();
            q.pop();
            if (state == target) {
                return steps;
            }
            for (int i = 0; i < 4; ++i) {
                int digit = state[i] - '0';
                for (int delta : {-1, 1}) {
                    std::string nxt = state;
                    nxt[i] = static_cast<char>('0' + (digit + delta + 10) % 10);
                    if (!seen.count(nxt) && !dead.count(nxt)) {
                        seen.insert(nxt);
                        q.push({nxt, steps + 1});
                    }
                }
            }
        }
        return -1;
    }
};
