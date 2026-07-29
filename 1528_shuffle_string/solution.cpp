// LeetCode 1528 - Shuffle String
// https://leetcode.com/problems/shuffle-string/

#include <string>
#include <vector>

class Solution {
public:
    std::string restoreString(std::string s, std::vector<int>& indices) {
        std::string answer(s.size(), ' ');
        for (std::size_t i = 0; i < s.size(); ++i) {
            answer[indices[i]] = s[i];
        }
        return answer;
    }
};
