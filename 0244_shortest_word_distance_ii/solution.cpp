// LeetCode 0244 - Shortest Word Distance II
// https://leetcode.com/problems/shortest-word-distance-ii/

#include <climits>
#include <string>
#include <unordered_map>
#include <vector>

class WordDistance {
    std::unordered_map<std::string, std::vector<int>> positions;

public:
    WordDistance(std::vector<std::string>& wordsDict) {
        for (int index = 0; index < static_cast<int>(wordsDict.size()); ++index) {
            positions[wordsDict[index]].push_back(index);
        }
    }

    int shortest(std::string word1, std::string word2) {
        const std::vector<int>& left = positions[word1];
        const std::vector<int>& right = positions[word2];
        int i = 0;
        int j = 0;
        int best = INT_MAX;
        while (i < static_cast<int>(left.size()) && j < static_cast<int>(right.size())) {
            best = std::min(best, std::abs(left[i] - right[j]));
            if (left[i] <= right[j]) {
                ++i;
            } else {
                ++j;
            }
        }
        return best;
    }
};
