// LeetCode 0839 - Similar String Groups
// https://leetcode.com/problems/similar-string-groups/

#include <string>
#include <vector>

class Solution {
public:
    int numSimilarGroups(std::vector<std::string>& strs) {
        int n = static_cast<int>(strs.size());
        std::vector<int> parent(n);
        for (int i = 0; i < n; ++i) {
            parent[i] = i;
        }
        auto find = [&](int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        };
        auto similar = [](const std::string& a, const std::string& b) {
            std::vector<int> diff;
            for (size_t i = 0; i < a.size(); ++i) {
                if (a[i] != b[i]) {
                    diff.push_back(static_cast<int>(i));
                    if (diff.size() > 2) {
                        return false;
                    }
                }
            }
            return diff.empty() ||
                   (diff.size() == 2 && a[diff[0]] == b[diff[1]] &&
                    a[diff[1]] == b[diff[0]]);
        };

        int groups = n;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (similar(strs[i], strs[j])) {
                    int pi = find(i), pj = find(j);
                    if (pi != pj) {
                        parent[pi] = pj;
                        --groups;
                    }
                }
            }
        }
        return groups;
    }
};
