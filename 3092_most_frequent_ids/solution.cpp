// LeetCode 3092 - Most Frequent IDs
// https://leetcode.com/problems/most-frequent-ids/

#include <queue>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<long long> mostFrequentIDs(std::vector<int>& nums, std::vector<int>& freq) {
        int n = (int)nums.size();
        std::unordered_map<int, int> cnt, lazy;
        std::vector<long long> ans(n);
        std::priority_queue<int> pq;
        for (int i = 0; i < n; i++) {
            int x = nums[i], f = freq[i];
            lazy[cnt[x]]++;
            cnt[x] += f;
            pq.push(cnt[x]);
            while (!pq.empty() && lazy[pq.top()] > 0) {
                lazy[pq.top()]--;
                pq.pop();
            }
            if (!pq.empty()) ans[i] = pq.top();
        }
        return ans;
    }
};
