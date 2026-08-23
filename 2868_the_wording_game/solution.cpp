// LeetCode 2868 - The Wording Game
// https://leetcode.com/problems/the-wording-game/

#include <string>
#include <vector>

class Solution {
public:
    bool canAliceWin(std::vector<std::string>& a, std::vector<std::string>& b) {
        int i = 0, j = 0;
        char last = 0;
        bool alice = true;
        while (true) {
            if (alice) {
                while (i < (int)a.size() && a[i][0] <= last) i++;
                if (i == (int)a.size()) return false;
                last = a[i].back();
                i++;
            } else {
                while (j < (int)b.size() && b[j][0] <= last) j++;
                if (j == (int)b.size()) return true;
                last = b[j].back();
                j++;
            }
            alice = !alice;
        }
    }
};
