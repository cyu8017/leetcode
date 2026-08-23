// LeetCode 1111 - Maximum Nesting Depth of Two Valid Parentheses Strings
// https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> maxDepthAfterSplit(std::string seq) {
        int depth = 0;
        std::vector<int> ans(seq.size());
        for (size_t i = 0; i < seq.size(); ++i) {
            if (seq[i] == '(') {
                ans[i] = depth % 2;
                ++depth;
            } else {
                --depth;
                ans[i] = depth % 2;
            }
        }
        return ans;
    }
};
