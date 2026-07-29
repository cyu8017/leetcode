// LeetCode 1258 - Synonymous Sentences
// https://leetcode.com/problems/synonymous-sentences/

#include <algorithm>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::string> generateSentences(std::vector<std::vector<std::string>>& synonyms, std::string text) {
        std::unordered_map<std::string, std::string> parent;
        auto find = [&](auto&& self, const std::string& x) -> std::string {
            if (!parent.count(x)) {
                parent[x] = x;
            }
            if (parent[x] != x) {
                parent[x] = self(self, parent[x]);
            }
            return parent[x];
        };
        for (const auto& pair : synonyms) {
            parent[find(find, pair[0])] = find(find, pair[1]);
        }
        std::unordered_map<std::string, std::vector<std::string>> groups;
        for (const auto& [word, _] : parent) {
            groups[find(find, word)].push_back(word);
        }
        for (auto& [_, words] : groups) {
            std::sort(words.begin(), words.end());
        }
        std::istringstream iss(text);
        std::vector<std::string> tokens;
        for (std::string w; iss >> w;) {
            tokens.push_back(w);
        }
        std::vector<std::vector<std::string>> choices;
        for (const std::string& w : tokens) {
            if (parent.count(w)) {
                choices.push_back(groups[find(find, w)]);
            } else {
                choices.push_back({w});
            }
        }
        std::vector<std::string> answer;
        std::vector<std::string> current;
        auto dfs = [&](auto&& self, int i) -> void {
            if (i == static_cast<int>(choices.size())) {
                std::string sentence = current[0];
                for (int j = 1; j < static_cast<int>(current.size()); ++j) {
                    sentence += " " + current[j];
                }
                answer.push_back(sentence);
                return;
            }
            for (const std::string& w : choices[i]) {
                current.push_back(w);
                self(self, i + 1);
                current.pop_back();
            }
        };
        dfs(dfs, 0);
        return answer;
    }
};
