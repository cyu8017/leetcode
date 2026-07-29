// LeetCode 0753 - Cracking the Safe
// https://leetcode.com/problems/cracking-the-safe/

#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::string crackSafe(int n, int k) {
        seen_.clear();
        path_.clear();
        std::string start(n - 1, '0');
        dfs(start, k);
        std::string result;
        for (char ch : path_) {
            result.push_back(ch);
        }
        return result + start;
    }

private:
    std::unordered_set<std::string> seen_;
    std::vector<char> path_;

    void dfs(const std::string& node, int k) {
        for (int d = 0; d < k; ++d) {
            char digit = static_cast<char>('0' + d);
            std::string edge = node + digit;
            if (!seen_.count(edge)) {
                seen_.insert(edge);
                dfs(edge.substr(1), k);
                path_.push_back(digit);
            }
        }
    }
};
