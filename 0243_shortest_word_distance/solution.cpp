// LeetCode 0243 - Shortest Word Distance
// https://leetcode.com/problems/shortest-word-distance/

#include <string>
#include <vector>
#include <climits>

class Solution {
public:
    int shortestWordDistance(std::vector<std::string>& wordsDict, std::string word1, std::string word2) {
        int index1 = -1;
        int index2 = -1;
        int best = INT_MAX;
        for (int index = 0; index < static_cast<int>(wordsDict.size()); ++index) {
            const std::string& word = wordsDict[index];
            if (word == word1) {
                index1 = index;
                if (index2 >= 0) {
                    best = std::min(best, index - index2);
                }
            }
            if (word == word2) {
                index2 = index;
                if (index1 >= 0) {
                    best = std::min(best, index - index1);
                }
            }
        }
        return best;
    }
};
