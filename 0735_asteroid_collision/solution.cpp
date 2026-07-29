// LeetCode 0735 - Asteroid Collision
// https://leetcode.com/problems/asteroid-collision/

#include <vector>

class Solution {
public:
    std::vector<int> asteroidCollision(std::vector<int>& asteroids) {
        std::vector<int> stack;
        for (int asteroid : asteroids) {
            bool alive = true;
            while (alive && !stack.empty() && asteroid < 0 && stack.back() > 0) {
                if (stack.back() < -asteroid) {
                    stack.pop_back();
                    continue;
                }
                if (stack.back() == -asteroid) {
                    stack.pop_back();
                }
                alive = false;
            }
            if (alive) {
                stack.push_back(asteroid);
            }
        }
        return stack;
    }
};
