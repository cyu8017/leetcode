// LeetCode 2593 - Find Score of an Array After Marking All Elements
// https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long findScore(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> idx(n);
        for (int i = 0; i < n; ++i) idx[i] = i;
        std::sort(idx.begin(), idx.end(), [&](int a, int b) {
            if (nums[a] != nums[b]) return nums[a] < nums[b];
            return a < b;
        });
        std::vector<char> marked(n, 0);
        long long ans = 0;
        for (int i : idx) {
            if (marked[i]) continue;
            ans += nums[i];
            marked[i] = 1;
            if (i > 0) marked[i - 1] = 1;
            if (i + 1 < n) marked[i + 1] = 1;
        }
        return ans;
    }
};
