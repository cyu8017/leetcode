// LeetCode 1239 - Maximum Length of a Concatenated String with Unique Characters
// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

#include <algorithm>
#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    int maxLength(std::vector<std::string>& arr) {
        std::vector<std::pair<int, int>> masks{{0, 0}};
        for (const std::string& word : arr) {
            int mask = 0;
            bool valid = true;
            for (char ch : word) {
                int bit = 1 << (ch - 'a');
                if (mask & bit) {
                    valid = false;
                    break;
                }
                mask |= bit;
            }
            if (!valid || __builtin_popcount(mask) != static_cast<int>(word.size())) {
                continue;
            }
            const int sz = static_cast<int>(masks.size());
            for (int i = 0; i < sz; ++i) {
                auto [used, length] = masks[i];
                if ((used & mask) == 0) {
                    masks.push_back({used | mask, length + static_cast<int>(word.size())});
                }
            }
        }
        int best = 0;
        for (const auto& [_, length] : masks) {
            best = std::max(best, length);
        }
        return best;
    }
};
