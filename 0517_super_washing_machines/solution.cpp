// LeetCode 0517 - Super Washing Machines
// https://leetcode.com/problems/super-washing-machines/

#include <algorithm>
#include <cstdlib>
#include <vector>

class Solution {
public:
    int findMinMoves(std::vector<int>& machines) {
        long long total = 0;
        for (const int clothes : machines) {
            total += clothes;
        }
        const int count = static_cast<int>(machines.size());
        if (total % count != 0) {
            return -1;
        }
        const int target = static_cast<int>(total / count);
        long long prefix = 0;
        int result = 0;
        for (const int clothes : machines) {
            const int diff = clothes - target;
            prefix += diff;
            result = std::max(result, std::max(static_cast<int>(std::llabs(prefix)), diff));
        }
        return result;
    }
};
