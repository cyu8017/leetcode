// LeetCode 0765 - Couples Holding Hands
// https://leetcode.com/problems/couples-holding-hands/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int minSwapsCouples(std::vector<int>& row) {
        std::unordered_map<int, int> pos;
        for (int i = 0; i < static_cast<int>(row.size()); ++i) {
            pos[row[i]] = i;
        }
        int swaps = 0;
        for (int i = 0; i < static_cast<int>(row.size()); i += 2) {
            int partner = row[i] ^ 1;
            if (row[i + 1] == partner) {
                continue;
            }
            int j = pos[partner];
            pos[row[i + 1]] = j;
            row[j] = row[i + 1];
            row[i + 1] = partner;
            pos[partner] = i + 1;
            ++swaps;
        }
        return swaps;
    }
};
