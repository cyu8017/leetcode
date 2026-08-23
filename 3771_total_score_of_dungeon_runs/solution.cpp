// LeetCode 3771 - Total Score of Dungeon Runs
// https://leetcode.com/problems/total-score-of-dungeon-runs/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long totalScore(int hp, std::vector<int>& damage, std::vector<int>& requirement) {
        int n = (int)damage.size();
        std::vector<long long> prefix(n + 1);
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + damage[i];
        long long answer = 1LL * n * (n + 1) / 2;
        for (int j = 1; j <= n; j++) {
            long long threshold = prefix[j] + (requirement[j - 1] - hp);
            int invalid = (int)(std::lower_bound(prefix.begin(), prefix.begin() + j, threshold) - prefix.begin());
            answer -= invalid;
        }
        return answer;
    }
};
