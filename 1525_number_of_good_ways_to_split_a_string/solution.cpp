// LeetCode 1525 - Number of Good Ways to Split a String
// https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

#include <string>
#include <unordered_map>
#include <unordered_set>

class Solution {
public:
    int numSplits(std::string s) {
        std::unordered_map<char, int> right;
        for (char ch : s) {
            right[ch] += 1;
        }
        std::unordered_set<char> left;
        int answer = 0;
        for (std::size_t i = 0; i + 1 < s.size(); ++i) {
            char ch = s[i];
            left.insert(ch);
            right[ch] -= 1;
            if (right[ch] == 0) {
                right.erase(ch);
            }
            if (left.size() == right.size()) {
                answer += 1;
            }
        }
        return answer;
    }
};
