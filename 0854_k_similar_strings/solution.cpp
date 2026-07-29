// LeetCode 0854 - K-Similar Strings
// https://leetcode.com/problems/k-similar-strings/

#include <queue>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int kSimilarity(std::string s1, std::string s2) {
        if (s1 == s2) {
            return 0;
        }
        std::queue<std::pair<std::string, int>> queue;
        queue.push({s1, 0});
        std::unordered_set<std::string> seen{s1};
        auto neighbors = [&](const std::string& s) {
            std::string arr = s;
            int i = 0;
            while (arr[i] == s2[i]) {
                ++i;
            }
            std::vector<std::string> res;
            for (int j = i + 1; j < static_cast<int>(arr.size()); ++j) {
                if (arr[j] == s2[i] && arr[j] != s2[j]) {
                    std::swap(arr[i], arr[j]);
                    res.push_back(arr);
                    std::swap(arr[i], arr[j]);
                }
            }
            return res;
        };
        while (!queue.empty()) {
            auto [cur, dist] = queue.front();
            queue.pop();
            for (const auto& nxt : neighbors(cur)) {
                if (nxt == s2) {
                    return dist + 1;
                }
                if (!seen.count(nxt)) {
                    seen.insert(nxt);
                    queue.push({nxt, dist + 1});
                }
            }
        }
        return -1;
    }
};
