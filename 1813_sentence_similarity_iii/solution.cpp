// LeetCode 1813 - Sentence Similarity III
// https://leetcode.com/problems/sentence-similarity-iii/

#include <sstream>
#include <string>
#include <vector>

class Solution {
public:
    bool areSentencesSimilar(std::string sentence1, std::string sentence2) {
        auto split = [](const std::string& s) {
            std::istringstream iss(s);
            std::vector<std::string> words;
            std::string word;
            while (iss >> word) {
                words.push_back(word);
            }
            return words;
        };

        std::vector<std::string> words1 = split(sentence1);
        std::vector<std::string> words2 = split(sentence2);
        int n1 = static_cast<int>(words1.size());
        int n2 = static_cast<int>(words2.size());

        int i = 0;
        while (i < n1 && i < n2 && words1[i] == words2[i]) {
            ++i;
        }
        if (i == n1 || i == n2) {
            return true;
        }

        int j1 = n1 - 1;
        int j2 = n2 - 1;
        while (j1 >= i && j2 >= i && words1[j1] == words2[j2]) {
            --j1;
            --j2;
        }
        return j1 < i || j2 < i;
    }
};
