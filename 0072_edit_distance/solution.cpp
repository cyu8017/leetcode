// LeetCode 0072 - Edit Distance
// https://leetcode.com/problems/edit-distance/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int minDistance(std::string word1, std::string word2) {
        int m = static_cast<int>(word1.size());
        int n = static_cast<int>(word2.size());
        std::vector<int> prev(n + 1);
        std::vector<int> curr(n + 1);

        for (int j = 0; j <= n; j++) {
            prev[j] = j;
        }

        for (int i = 1; i <= m; i++) {
            curr[0] = i;
            for (int j = 1; j <= n; j++) {
                if (word1[i - 1] == word2[j - 1]) {
                    curr[j] = prev[j - 1];
                } else {
                    curr[j] = 1 + std::min({prev[j], curr[j - 1], prev[j - 1]});
                }
            }
            prev.swap(curr);
        }

        return prev[n];
    }
};
