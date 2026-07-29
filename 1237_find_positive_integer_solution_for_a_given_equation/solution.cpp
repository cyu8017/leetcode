// LeetCode 1237 - Find Positive Integer Solution for a Given Equation
// https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

#include <vector>

class CustomFunction {
public:
    int f(int x, int y);
};

class Solution {
public:
    std::vector<std::vector<int>> findSolution(CustomFunction& customfunction, int z) {
        std::vector<std::vector<int>> answer;
        int x = 1, y = 1000;
        while (x <= 1000 && y >= 1) {
            int value = customfunction.f(x, y);
            if (value == z) {
                answer.push_back({x, y});
                ++x;
                --y;
            } else if (value < z) {
                ++x;
            } else {
                --y;
            }
        }
        return answer;
    }
};
