// LeetCode 1817 - Finding the Users Active Minutes
// https://leetcode.com/problems/finding-the-users-active-minutes/

#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<int> findingUsersActiveMinutes(std::vector<std::vector<int>>& logs, int k) {
        std::unordered_map<int, std::unordered_set<int>> userMinutes;
        for (const auto& entry : logs) {
            userMinutes[entry[0]].insert(entry[1]);
        }
        std::vector<int> answer(k, 0);
        for (const auto& [userId, minutes] : userMinutes) {
            (void)userId;
            int uam = static_cast<int>(minutes.size());
            if (uam <= k) {
                answer[uam - 1] += 1;
            }
        }
        return answer;
    }
};
