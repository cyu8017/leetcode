// LeetCode 1079 - Letter Tile Possibilities
// https://leetcode.com/problems/letter-tile-possibilities/

#include <functional>
#include <string>
#include <vector>

class Solution {
public:
    int numTilePossibilities(std::string tiles) {
        std::vector<int> count(26, 0);
        for (char ch : tiles) {
            ++count[ch - 'A'];
        }

        std::function<int()> dfs = [&]() -> int {
            int total = 0;
            for (int i = 0; i < 26; ++i) {
                if (count[i] == 0) {
                    continue;
                }
                --count[i];
                total += 1 + dfs();
                ++count[i];
            }
            return total;
        };

        return dfs();
    }
};
