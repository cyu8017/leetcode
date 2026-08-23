// LeetCode 3362 - Zero Array Transformation III
// https://leetcode.com/problems/zero-array-transformation-iii/

#include <algorithm>
#include <queue>
#include <vector>

class Solution {
public:
    int maxRemoval(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        std::sort(queries.begin(), queries.end(), [](auto& a, auto& b) { return a[0] < b[0]; });
        std::priority_queue<int> h;
        int n = (int)nums.size();
        std::vector<int> diff(n + 1);
        int j = 0, used = 0, cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            while (j < (int)queries.size() && queries[j][0] == i) {
                h.push(queries[j][1]);
                j++;
            }
            while (cur < nums[i]) {
                if (h.empty() || h.top() < i) return -1;
                int r = h.top();
                h.pop();
                cur++;
                diff[r + 1]--;
                used++;
            }
        }
        return (int)queries.size() - used;
    }
};
