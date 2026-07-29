#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int maxStudents(std::vector<std::vector<std::string>>& seats) {
        int rows = (int)seats.size(), cols = (int)seats[0].size();
        std::vector<std::vector<int>> validRows;
        for (auto& row : seats) {
            int available = 0;
            for (int c = 0; c < cols; ++c)
                if (row[c] == ".") available |= 1 << c;
            std::vector<int> masks;
            for (int mask = 0; mask < (1 << cols); ++mask)
                if ((mask & ~available) == 0 && (mask & (mask << 1)) == 0) masks.push_back(mask);
            validRows.push_back(masks);
        }
        std::unordered_map<int, int> dp{{0, 0}};
        for (auto& masks : validRows) {
            std::unordered_map<int, int> nxt;
            for (int mask : masks) {
                for (auto [previous, count] : dp) {
                    if ((mask & (previous << 1)) == 0 && (mask & (previous >> 1)) == 0) {
                        int bits = __builtin_popcount(mask);
                        nxt[mask] = std::max(nxt.count(mask) ? nxt[mask] : 0, count + bits);
                    }
                }
            }
            dp = std::move(nxt);
        }
        int answer = 0;
        for (auto [_, v] : dp) answer = std::max(answer, v);
        return answer;
    }
};
