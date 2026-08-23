// LeetCode 3080 - Mark Elements on Array by Performing Queries
// https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<long long> unmarkedSumArray(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        long long s = 0;
        for (int x : nums) s += x;
        std::vector<char> mark(n, 0);
        std::vector<std::pair<int, int>> arr;
        arr.reserve(n);
        for (int i = 0; i < n; i++) arr.push_back({nums[i], i});
        std::sort(arr.begin(), arr.end());
        std::vector<long long> ans(queries.size());
        int j = 0;
        for (int qi = 0; qi < (int)queries.size(); qi++) {
            int index = queries[qi][0], k = queries[qi][1];
            if (!mark[index]) {
                mark[index] = 1;
                s -= nums[index];
            }
            for (; k > 0 && j < n; j++) {
                if (!mark[arr[j].second]) {
                    mark[arr[j].second] = 1;
                    s -= arr[j].first;
                    k--;
                }
            }
            ans[qi] = s;
        }
        return ans;
    }
};
