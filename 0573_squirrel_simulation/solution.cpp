// LeetCode 0573 - Squirrel Simulation
// https://leetcode.com/problems/squirrel-simulation/

#include <cstdlib>
#include <vector>

class Solution {
public:
    int minDistance(int height, int width, std::vector<int>& tree, std::vector<int>& squirrel,
                    std::vector<std::vector<int>>& nuts) {
        (void)height;
        (void)width;
        int total = 0;
        int bestSave = -2147483647;
        for (const std::vector<int>& nut : nuts) {
            int treeDist = dist(tree, nut);
            int squirrelDist = dist(squirrel, nut);
            total += 2 * treeDist;
            int save = treeDist - squirrelDist;
            if (save > bestSave) {
                bestSave = save;
            }
        }
        return total - bestSave;
    }

private:
    int dist(const std::vector<int>& a, const std::vector<int>& b) {
        return std::abs(a[0] - b[0]) + std::abs(a[1] - b[1]);
    }
};
