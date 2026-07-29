// LeetCode 0809 - Expressive Words
// https://leetcode.com/problems/expressive-words/

#include <string>
#include <utility>
#include <vector>

class Solution {
public:
    int expressiveWords(std::string s, std::vector<std::string>& words) {
        auto groups = [](const std::string& text) {
            std::vector<std::pair<char, int>> result;
            int i = 0, n = static_cast<int>(text.size());
            while (i < n) {
                int j = i;
                while (j < n && text[j] == text[i]) {
                    ++j;
                }
                result.push_back({text[i], j - i});
                i = j;
            }
            return result;
        };

        auto target = groups(s);
        int ans = 0;
        for (const auto& word : words) {
            auto source = groups(word);
            if (source.size() != target.size()) {
                continue;
            }
            bool ok = true;
            for (size_t i = 0; i < source.size(); ++i) {
                if (source[i].first != target[i].first) {
                    ok = false;
                    break;
                }
                int c1 = source[i].second, c2 = target[i].second;
                if (c1 > c2 || (c1 != c2 && c2 < 3)) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                ++ans;
            }
        }
        return ans;
    }
};
