// LeetCode 3996 - Even Number of Knight Moves
// https://leetcode.com/problems/even-number-of-knight-moves/

#include <vector>

class Solution {
public:
    bool canReach(std::vector<int>& start, std::vector<int>& target) {
        return ((start[0] + start[1]) % 2) == ((target[0] + target[1]) % 2);
    }
};
