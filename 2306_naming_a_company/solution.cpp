// LeetCode 2306 - Naming a Company
// https://leetcode.com/problems/naming-a-company/

#include <vector>
#include <string>
#include <unordered_set>

class Solution {
public:
    long long distinctNames(std::vector<std::string>& ideas) {
        std::vector<std::unordered_set<std::string>> groups(26);
        for (auto& idea : ideas) groups[idea[0] - 'a'].insert(idea.substr(1));
        long long ans = 0;
        for (int i = 0; i < 26; ++i) {
            for (int j = i + 1; j < 26; ++j) {
                int overlap = 0;
                for (auto& s : groups[i]) if (groups[j].count(s)) overlap++;
                ans += 1LL * ((int)groups[i].size() - overlap) * ((int)groups[j].size() - overlap) * 2;
            }
        }
        return ans;
    }
};
