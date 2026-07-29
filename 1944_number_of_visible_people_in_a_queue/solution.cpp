// LeetCode 1944 - Number of Visible People in a Queue
#include <vector>

class Solution {
public:
    std::vector<int> canSeePersonsCount(std::vector<int>& heights) {
        int n = (int)heights.size();
        std::vector<int> ans(n), stack;
        for (int i = n - 1; i >= 0; i--) {
            int count = 0;
            while (!stack.empty() && heights[i] > stack.back()) {
                stack.pop_back();
                count++;
            }
            if (!stack.empty()) count++;
            ans[i] = count;
            stack.push_back(heights[i]);
        }
        return ans;
    }
};
