#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::string rankTeams(std::vector<std::string>& votes) {
        int m = (int)votes[0].size();
        std::unordered_map<char, std::vector<int>> count;
        for (char c : votes[0]) count[c].assign(m, 0);
        for (auto& v : votes)
            for (int i = 0; i < m; ++i) ++count[v[i]][i];
        std::string teams = votes[0];
        std::sort(teams.begin(), teams.end(), [&](char a, char b) {
            if (count[a] != count[b]) return count[a] > count[b];
            return a < b;
        });
        return teams;
    }
};
