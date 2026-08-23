// LeetCode 0593 - Valid Square
// https://leetcode.com/problems/valid-square/

#include <algorithm>
#include <vector>

class Solution {
public:
    bool validSquare(std::vector<int>& p1, std::vector<int>& p2, std::vector<int>& p3,
                     std::vector<int>& p4) {
        std::vector<int>* points[4] = {&p1, &p2, &p3, &p4};
        std::vector<int> distances;
        distances.reserve(6);
        for (int i = 0; i < 4; ++i) {
            for (int j = i + 1; j < 4; ++j) {
                distances.push_back(distSq(*points[i], *points[j]));
            }
        }
        std::sort(distances.begin(), distances.end());
        return distances[0] > 0 && distances[0] == distances[1] && distances[1] == distances[2] &&
               distances[2] == distances[3] && distances[4] == distances[5] &&
               distances[4] == 2 * distances[0];
    }

private:
    int distSq(const std::vector<int>& a, const std::vector<int>& b) {
        int dx = a[0] - b[0];
        int dy = a[1] - b[1];
        return dx * dx + dy * dy;
    }
};
