// LeetCode 0881 - Boats to Save People
// https://leetcode.com/problems/boats-to-save-people/

#include <algorithm>
#include <vector>

class Solution {
public:
    int numRescueBoats(std::vector<int>& people, int limit) {
        std::sort(people.begin(), people.end());
        int i = 0, j = static_cast<int>(people.size()) - 1, boats = 0;
        while (i <= j) {
            if (people[i] + people[j] <= limit) {
                ++i;
            }
            --j;
            ++boats;
        }
        return boats;
    }
};
