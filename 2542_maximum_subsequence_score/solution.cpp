// LeetCode 2542 - Maximum Subsequence Score
// https://leetcode.com/problems/maximum-subsequence-score/

#include <algorithm>
#include <queue>
#include <vector>

class Solution {
public:
    long long maxScore(std::vector<int>& nums1, std::vector<int>& nums2, int k) {
        int n = (int)nums1.size();
        std::vector<int> idx(n);
        for (int i = 0; i < n; i++) idx[i] = i;
        std::sort(idx.begin(), idx.end(), [&](int a, int b) { return nums2[a] > nums2[b]; });
        std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
        long long sum = 0, ans = 0;
        for (int i : idx) {
            pq.push(nums1[i]);
            sum += nums1[i];
            if ((int)pq.size() > k) {
                sum -= pq.top();
                pq.pop();
            }
            if ((int)pq.size() == k) {
                long long cand = sum * nums2[i];
                if (cand > ans) ans = cand;
            }
        }
        return ans;
    }
};
