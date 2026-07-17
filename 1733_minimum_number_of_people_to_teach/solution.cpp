// LeetCode 1733 - Minimum Number of People to Teach
// https://leetcode.com/problems/minimum-number-of-people-to-teach/

#include <algorithm>
#include <climits>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int minimumTeachings(int n, std::vector<std::vector<int>>& languages, std::vector<std::vector<int>>& friendships) {
        int users = languages.size();
        std::vector<std::vector<bool>> knows(users, std::vector<bool>(n + 1, false));
        for (int user = 0; user < users; user++) {
            for (int lang : languages[user]) {
                knows[user][lang] = true;
            }
        }
        std::unordered_set<int> need;
        for (const std::vector<int>& friendship : friendships) {
            int u = friendship[0] - 1;
            int v = friendship[1] - 1;
            bool shares = false;
            for (int lang : languages[u]) {
                if (knows[v][lang]) {
                    shares = true;
                    break;
                }
            }
            if (!shares) {
                need.insert(u);
                need.insert(v);
            }
        }
        if (need.empty()) {
            return 0;
        }
        int best = INT_MAX;
        for (int lang = 1; lang <= n; lang++) {
            int teach = 0;
            for (int user : need) {
                if (!knows[user][lang]) teach++;
            }
            best = std::min(best, teach);
        }
        return best;
    }
};
