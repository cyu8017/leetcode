#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<int> peopleIndexes(std::vector<std::vector<std::string>>& favoriteCompanies) {
        int n = (int)favoriteCompanies.size();
        std::vector<std::unordered_set<std::string>> sets(n);
        for (int i = 0; i < n; ++i)
            sets[i] = {favoriteCompanies[i].begin(), favoriteCompanies[i].end()};
        std::vector<int> answer;
        for (int i = 0; i < n; ++i) {
            bool subset = false;
            for (int j = 0; j < n && !subset; ++j) {
                if (i == j) continue;
                bool isSub = true;
                for (auto& c : sets[i]) if (!sets[j].count(c)) { isSub = false; break; }
                if (isSub) subset = true;
            }
            if (!subset) answer.push_back(i);
        }
        return answer;
    }
};
