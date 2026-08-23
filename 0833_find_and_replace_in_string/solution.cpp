// LeetCode 0833 - Find And Replace in String
// https://leetcode.com/problems/find-and-replace-in-string/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::string findReplaceString(std::string s, std::vector<int>& indices,
                                  std::vector<std::string>& sources,
                                  std::vector<std::string>& targets) {
        std::unordered_map<int, std::pair<int, std::string>> replace;
        for (size_t k = 0; k < indices.size(); ++k) {
            int i = indices[k];
            if (s.compare(i, sources[k].size(), sources[k]) == 0) {
                replace[i] = {static_cast<int>(sources[k].size()), targets[k]};
            }
        }
        std::string out;
        int i = 0, n = static_cast<int>(s.size());
        while (i < n) {
            if (replace.count(i)) {
                out += replace[i].second;
                i += replace[i].first;
            } else {
                out.push_back(s[i]);
                ++i;
            }
        }
        return out;
    }
};
