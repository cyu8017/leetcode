// LeetCode 0293 - Flip Game
// https://leetcode.com/problems/flip-game/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> generatePossibleNextMoves(std::string currentState) {
        std::vector<std::string> result;
        for (int index = 0; index + 1 < static_cast<int>(currentState.size()); index++) {
            if (currentState[index] == '+' && currentState[index + 1] == '+') {
                std::string nextState = currentState;
                nextState[index] = '-';
                nextState[index + 1] = '-';
                result.push_back(nextState);
            }
        }
        return result;
    }
};
