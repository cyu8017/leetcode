// LeetCode 3321 - Find X-Sum of All K-Long Subarrays II
// https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<long long> findXSum(std::vector<int>& nums, int k, int x) {
        int n = (int)nums.size();
        std::vector<long long> ans(n - k + 1);
        for (int i = 0; i <= n - k; i++) {
            std::unordered_map<int, int> freq;
            for (int j = i; j < i + k; j++) freq[nums[j]]++;
            struct P { int v, f; };
            std::vector<P> arr;
            for (auto& p : freq) arr.push_back({p.first, p.second});
            for (int a = 0; a < (int)arr.size(); a++) {
                for (int b = a + 1; b < (int)arr.size(); b++) {
                    if (arr[b].f > arr[a].f || (arr[b].f == arr[a].f && arr[b].v > arr[a].v))
                        std::swap(arr[a], arr[b]);
                }
            }
            int lim = std::min(x, (int)arr.size());
            std::unordered_map<int, char> keep;
            for (int t = 0; t < lim; t++) keep[arr[t].v] = 1;
            long long sum = 0;
            for (int j = i; j < i + k; j++) if (keep.count(nums[j])) sum += nums[j];
            ans[i] = sum;
        }
        return ans;
    }
};
