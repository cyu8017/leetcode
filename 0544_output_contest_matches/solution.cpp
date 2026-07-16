// LeetCode 0544 - Output Contest Matches
// https://leetcode.com/problems/output-contest-matches/

#include <string>
#include <vector>

class Solution {
public:
    std::string findContestMatch(int n) {
        std::vector<std::string> teams;
        teams.reserve(n);
        for (int team = 1; team <= n; ++team) {
            teams.push_back(std::to_string(team));
        }

        while (teams.size() > 1) {
            std::vector<std::string> nextRound;
            nextRound.reserve(teams.size() / 2);
            for (size_t index = 0; index < teams.size() / 2; ++index) {
                nextRound.push_back("(" + teams[index] + "," + teams[teams.size() - 1 - index] + ")");
            }
            teams.swap(nextRound);
        }

        return teams[0];
    }
};
