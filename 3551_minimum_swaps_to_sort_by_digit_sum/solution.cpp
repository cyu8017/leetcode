// LeetCode 3551 - Minimum Swaps to Sort by Digit Sum
// https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/

#include <vector>
#include <algorithm>
#include <unordered_map>
#include <array>

class Solution {
    int f(int x) {
        int s = 0;
        while (x) { s += x % 10; x /= 10; }
        return s;
    }
public:
    int minSwaps(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<std::array<int, 2>> arr(n);
        for (int i = 0; i < n; i++) arr[i] = {f(nums[i]), nums[i]};
        std::sort(arr.begin(), arr.end(), [](auto& a, auto& b) {
            if (a[0] != b[0]) return a[0] < b[0];
            return a[1] < b[1];
        });
        std::unordered_map<int, int> d;
        for (int i = 0; i < n; i++) d[arr[i][1]] = i;
        std::vector<char> vis(n);
        int ans = n;
        for (int i = 0; i < n; i++) {
            if (!vis[i]) {
                ans--;
                int j = i;
                while (!vis[j]) {
                    vis[j] = 1;
                    j = d[nums[j]];
                }
            }
        }
        return ans;
    }
};
