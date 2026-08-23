// LeetCode 2942 - Find Words Containing Character
// https://leetcode.com/problems/find-words-containing-character/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> findWordsContaining(std::vector<std::string>& words, char x) {
        std::vector<int> ans;
        for (int i = 0; i < (int)words.size(); i++) {
            for (char c : words[i]) {
                if (c == x) {
                    ans.push_back(i);
                    break;
                }
            }
        }
        return ans;
    }
};
