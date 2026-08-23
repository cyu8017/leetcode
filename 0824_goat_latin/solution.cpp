// LeetCode 0824 - Goat Latin
// https://leetcode.com/problems/goat-latin/

#include <sstream>
#include <string>
#include <unordered_set>

class Solution {
public:
    std::string toGoatLatin(std::string sentence) {
        static const std::unordered_set<char> vowels = {
            'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        std::istringstream iss(sentence);
        std::string word, out;
        int i = 1;
        while (iss >> word) {
            if (!out.empty()) {
                out.push_back(' ');
            }
            std::string goat;
            if (vowels.count(word[0])) {
                goat = word + "ma";
            } else {
                goat = word.substr(1) + word[0] + "ma";
            }
            goat.append(i, 'a');
            out += goat;
            ++i;
        }
        return out;
    }
};
