// LeetCode 3926 - Count Valid Word Occurrences
// https://leetcode.com/problems/count-valid-word-occurrences/

#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> countWordOccurrences(std::vector<std::string>& chunks, std::vector<std::string>& queries) {
        std::string s;
        for (auto& c : chunks) s += c;
        int n = (int)s.size();
        std::unordered_map<std::string, int> cnt;
        int i = 0;
        while (i < n) {
            if (s[i] == ' ' || s[i] == '-') {
                i++;
                continue;
            }
            int j = i;
            while (j < n && s[j] != ' ' && (s[j] != '-' || (j + 1 < n && s[j + 1] != ' ' && s[j + 1] != '-'))) {
                j++;
            }
            cnt[s.substr(i, j - i)]++;
            i = j;
        }
        std::vector<int> ans(queries.size());
        for (int k = 0; k < (int)queries.size(); k++) ans[k] = cnt[queries[k]];
        return ans;
    }
};
