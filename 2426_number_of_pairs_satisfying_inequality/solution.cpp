// LeetCode 2426 - Number of Pairs Satisfying Inequality
// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

#include <vector>

class Solution {
public:
    long long numberOfPairs(std::vector<int>& nums1, std::vector<int>& nums2, int diff) {
        int n = (int)nums1.size();
        std::vector<int> arr(n), tmp(n);
        for (int i = 0; i < n; i++) arr[i] = nums1[i] - nums2[i];
        auto mergeCount = [&](auto&& self, int l, int r) -> long long {
            if (r - l <= 1) return 0;
            int m = (l + r) / 2;
            long long ans = self(self, l, m) + self(self, m, r);
            int j = m;
            for (int i = l; i < m; i++) {
                while (j < r && arr[j] < arr[i] - diff) j++;
                ans += r - j;
            }
            int i = l, p = l, q = m;
            while (p < m && q < r) {
                if (arr[p] <= arr[q]) tmp[i++] = arr[p++];
                else tmp[i++] = arr[q++];
            }
            while (p < m) tmp[i++] = arr[p++];
            while (q < r) tmp[i++] = arr[q++];
            for (int t = l; t < r; t++) arr[t] = tmp[t];
            return ans;
        };
        return mergeCount(mergeCount, 0, n);
    }
};
