// LeetCode 2672 - Number of Adjacent Elements With the Same Color
// https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

#include <vector>

class Solution {
public:
    std::vector<int> colorTheArray(int n, std::vector<std::vector<int>>& queries) {
        std::vector<int> colors(n), ans(queries.size());
        int same = 0;
        for (int i = 0; i < (int)queries.size(); i++) {
            int idx = queries[i][0], color = queries[i][1];
            if (colors[idx] != 0) {
                if (idx > 0 && colors[idx] == colors[idx - 1]) same--;
                if (idx + 1 < n && colors[idx] == colors[idx + 1]) same--;
            }
            colors[idx] = color;
            if (idx > 0 && colors[idx] == colors[idx - 1]) same++;
            if (idx + 1 < n && colors[idx] == colors[idx + 1]) same++;
            ans[i] = same;
        }
        return ans;
    }
};
