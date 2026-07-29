// LeetCode 0756 - Pyramid Transition Matrix
// https://leetcode.com/problems/pyramid-transition-matrix/

#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool pyramidTransition(std::string bottom, std::vector<std::string>& allowed) {
        transitions_.clear();
        memo_.clear();
        for (const std::string& triple : allowed) {
            transitions_[triple.substr(0, 2)].push_back(triple[2]);
        }
        return dfs(bottom);
    }

private:
    std::unordered_map<std::string, std::vector<char>> transitions_;
    std::unordered_map<std::string, bool> memo_;

    bool dfs(const std::string& row) {
        if (row.size() == 1) {
            return true;
        }
        auto it = memo_.find(row);
        if (it != memo_.end()) {
            return it->second;
        }
        std::vector<std::vector<char>> options;
        for (size_t i = 0; i + 1 < row.size(); ++i) {
            std::string key = row.substr(i, 2);
            auto found = transitions_.find(key);
            if (found == transitions_.end()) {
                return memo_[row] = false;
            }
            options.push_back(found->second);
        }
        std::string path;
        return memo_[row] = build(0, options, path);
    }

    bool build(size_t index, const std::vector<std::vector<char>>& options, std::string& path) {
        if (index == options.size()) {
            return dfs(path);
        }
        for (char ch : options[index]) {
            path.push_back(ch);
            if (build(index + 1, options, path)) {
                return true;
            }
            path.pop_back();
        }
        return false;
    }
};
