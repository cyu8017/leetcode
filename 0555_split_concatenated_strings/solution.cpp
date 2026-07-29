// LeetCode 0555 - Split Concatenated Strings
// https://leetcode.com/problems/split-concatenated-strings/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::string splitLoopedString(std::vector<std::string>& strs) {
        std::vector<std::string> bestForms;
        bestForms.reserve(strs.size());
        for (const std::string& s : strs) {
            std::string rev = s;
            std::reverse(rev.begin(), rev.end());
            bestForms.push_back(std::max(s, rev));
        }

        std::string answer;
        for (std::size_t i = 0; i < strs.size(); ++i) {
            std::string mid;
            for (std::size_t j = i + 1; j < strs.size(); ++j) {
                mid += bestForms[j];
            }
            for (std::size_t j = 0; j < i; ++j) {
                mid += bestForms[j];
            }

            std::string original = strs[i];
            std::string reversed = original;
            std::reverse(reversed.begin(), reversed.end());
            const std::string candidates[2] = {original, reversed};

            for (const std::string& candidate : candidates) {
                for (std::size_t cut = 0; cut < candidate.size(); ++cut) {
                    std::string formed = candidate.substr(cut) + mid + candidate.substr(0, cut);
                    if (formed > answer) {
                        answer = formed;
                    }
                }
            }
        }
        return answer;
    }
};
