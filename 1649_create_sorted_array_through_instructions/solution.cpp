// LeetCode 1649 - Create Sorted Array through Instructions
// https://leetcode.com/problems/create-sorted-array-through-instructions/

#include <algorithm>
#include <vector>

class Solution {
public:
    int createSortedArray(std::vector<int>& instructions) {
        const int MOD = 1000000007;
        const int size = *std::max_element(instructions.begin(), instructions.end()) + 2;
        std::vector<int> bit(size + 1, 0);
        auto query = [&](int i) {
            int s = 0;
            while (i) {
                s += bit[i];
                i -= i & -i;
            }
            return s;
        };
        auto update = [&](int i) {
            while (i <= size) {
                ++bit[i];
                i += i & -i;
            }
        };
        int ans = 0;
        for (int i = 0; i < static_cast<int>(instructions.size()); ++i) {
            const int x = instructions[i];
            ans = (ans + std::min(query(x - 1), i - query(x))) % MOD;
            update(x);
        }
        return ans;
    }
};
