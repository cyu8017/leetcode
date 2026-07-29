#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<int> luckyNumbers(std::vector<std::vector<int>>& matrix) {
        std::unordered_set<int> mins, maxs;
        for (auto& r : matrix) mins.insert(*std::min_element(r.begin(), r.end()));
        int n = (int)matrix[0].size(), m = (int)matrix.size();
        for (int c = 0; c < n; ++c) {
            int mx = matrix[0][c];
            for (int r = 1; r < m; ++r) mx = std::max(mx, matrix[r][c]);
            maxs.insert(mx);
        }
        std::vector<int> answer;
        for (int x : mins) if (maxs.count(x)) answer.push_back(x);
        return answer;
    }
};
