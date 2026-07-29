// LeetCode 1125 - Smallest Sufficient Team
// https://leetcode.com/problems/smallest-sufficient-team/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> smallestSufficientTeam(std::vector<std::string>& req_skills,
                                            std::vector<std::vector<std::string>>& people) {
        const int m = static_cast<int>(req_skills.size());
        const int n = static_cast<int>(people.size());
        const int target = (1 << m) - 1;
        std::unordered_map<std::string, int> skillId;
        for (int i = 0; i < m; ++i) skillId[req_skills[i]] = i;
        std::vector<int> personMasks(n, 0);
        for (int i = 0; i < n; ++i) {
            int mask = 0;
            for (const auto& skill : people[i]) mask |= 1 << skillId[skill];
            personMasks[i] = mask;
        }
        std::vector<long long> dp(1 << m, -1);
        dp[0] = 0;
        for (int state = 0; state <= target; ++state) {
            if (dp[state] < 0) continue;
            for (int i = 0; i < n; ++i) {
                const int next = state | personMasks[i];
                if (next == state) continue;
                const long long cand = dp[state] | (1LL << i);
                if (dp[next] < 0 || __builtin_popcountll(cand) < __builtin_popcountll(dp[next])) {
                    dp[next] = cand;
                }
            }
        }
        std::vector<int> ans;
        for (int i = 0; i < n; ++i) if (dp[target] & (1LL << i)) ans.push_back(i);
        return ans;
    }
};
