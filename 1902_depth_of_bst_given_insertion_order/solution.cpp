// LeetCode 1902 - Depth of BST Given Insertion Order
// https://leetcode.com/problems/depth-of-bst-given-insertion-order/

#include <algorithm>
#include <utility>
#include <vector>

class Solution {
public:
    int maxDepthBST(std::vector<int>& order) {
        std::vector<std::pair<int, int>> nodes;
        int ans = 0;
        for (int value : order) {
            auto it = std::lower_bound(nodes.begin(), nodes.end(), std::make_pair(value, 0));
            int depth = 1;
            int i = (int)(it - nodes.begin());
            if (i > 0) depth = std::max(depth, nodes[i - 1].second + 1);
            if (i < (int)nodes.size()) depth = std::max(depth, nodes[i].second + 1);
            nodes.insert(it, {value, depth});
            ans = std::max(ans, depth);
        }
        return ans;
    }
};
