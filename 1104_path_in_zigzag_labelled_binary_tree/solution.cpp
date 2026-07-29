// LeetCode 1104 - Path In Zigzag Labelled Binary Tree
// https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> pathInZigZagTree(int label) {
        std::vector<int> path;
        path.push_back(label);
        while (label > 1) {
            int level = 31 - __builtin_clz(label);
            label >>= 1;
            label = (1 << level) - 1 - label + (1 << (level - 1));
            path.push_back(label);
        }
        std::reverse(path.begin(), path.end());
        return path;
    }
};
