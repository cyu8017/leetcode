// LeetCode 1832 - Check if the Sentence Is Pangram
// https://leetcode.com/problems/check-if-the-sentence-is-pangram/

#include <string>
#include <unordered_set>

class Solution {
public:
    bool checkIfPangram(std::string sentence) {
        return std::unordered_set<char>(sentence.begin(), sentence.end()).size() == 26;
    }
};
