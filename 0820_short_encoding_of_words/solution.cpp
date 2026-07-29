// LeetCode 0820 - Short Encoding of Words
// https://leetcode.com/problems/short-encoding-of-words/

#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int minimumLengthEncoding(std::vector<std::string>& words) {
        std::unordered_set<std::string> good(words.begin(), words.end());
        for (const auto& word : words) {
            for (size_t i = 1; i < word.size(); ++i) {
                good.erase(word.substr(i));
            }
        }
        int ans = 0;
        for (const auto& word : good) {
            ans += static_cast<int>(word.size()) + 1;
        }
        return ans;
    }
};
