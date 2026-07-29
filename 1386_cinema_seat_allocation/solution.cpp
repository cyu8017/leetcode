#include <unordered_map>
#include <vector>

class Solution {
public:
    int maxNumberOfFamilies(int n, std::vector<std::vector<int>>& reservedSeats) {
        std::unordered_map<int, int> rows;
        for (auto& s : reservedSeats) {
            int r = s[0], c = s[1];
            if (2 <= c && c <= 9) rows[r] |= 1 << (c - 2);
        }
        int ans = 2 * (n - (int)rows.size());
        for (auto [_, m] : rows) {
            bool left = (m & 0b00001111) == 0;
            bool right = (m & 0b11110000) == 0;
            bool middle = (m & 0b00111100) == 0;
            ans += (left && right) ? 2 : int(left || right || middle);
        }
        return ans;
    }
};
