// LeetCode 0957 - Prison Cells After N Days
// https://leetcode.com/problems/prison-cells-after-n-days/

#include <map>
#include <vector>

class Solution {
public:
    std::vector<int> prisonAfterNDays(std::vector<int>& cells, int n) {
        std::map<std::vector<int>, int> seen;
        std::vector<int> state = cells;
        while (n) {
            if (seen.count(state)) {
                int cycle = seen[state] - n;
                n %= cycle;
                if (n == 0) break;
            }
            seen[state] = n;
            std::vector<int> nxt(8, 0);
            for (int i = 1; i <= 6; i++) nxt[i] = state[i - 1] == state[i + 1] ? 1 : 0;
            state.swap(nxt);
            n--;
        }
        return state;
    }
};
