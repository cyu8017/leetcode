// LeetCode 3636 - Threshold Majority Queries
// https://leetcode.com/problems/threshold-majority-queries/

#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> subarrayMajority(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        std::vector<int> ans(queries.size());
        for (int qi = 0; qi < (int)queries.size(); qi++) {
            int l = queries[qi][0], r = queries[qi][1], thresh = queries[qi][2];
            std::unordered_map<int, int> freq;
            for (int i = l; i <= r; i++) freq[nums[i]]++;
            int bestVal = -1, bestCnt = 0;
            for (auto& [v, c] : freq) {
                if (c >= thresh && (c > bestCnt || (c == bestCnt && (bestVal == -1 || v < bestVal)))) {
                    bestCnt = c;
                    bestVal = v;
                }
            }
            ans[qi] = bestVal;
        }
        return ans;
    }
};
