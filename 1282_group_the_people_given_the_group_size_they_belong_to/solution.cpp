// LeetCode 1282 - Group the People Given the Group Size They Belong To
// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> groupThePeople(std::vector<int>& groupSizes) {
        std::unordered_map<int, std::vector<int>> pending;
        std::vector<std::vector<int>> answer;
        for (int person = 0; person < static_cast<int>(groupSizes.size()); ++person) {
            int size = groupSizes[person];
            pending[size].push_back(person);
            if (static_cast<int>(pending[size].size()) == size) {
                answer.push_back(pending[size]);
                pending[size].clear();
            }
        }
        std::sort(answer.begin(), answer.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            if (a.size() != b.size()) {
                return a.size() < b.size();
            }
            return a < b;
        });
        return answer;
    }
};
