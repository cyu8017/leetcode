// LeetCode 0781 - Rabbits in Forest
// https://leetcode.com/problems/rabbits-in-forest/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int numRabbits(std::vector<int>& answers) {
        std::unordered_map<int, int> counts;
        for (int answer : answers) {
            ++counts[answer];
        }
        int total = 0;
        for (auto [answer, count] : counts) {
            int group = answer + 1;
            int groups = (count + group - 1) / group;
            total += groups * group;
        }
        return total;
    }
};
