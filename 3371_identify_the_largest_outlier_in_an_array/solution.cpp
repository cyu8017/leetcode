// LeetCode 3371 - Identify the Largest Outlier in an Array
// https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

#include <climits>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int getLargestOutlier(std::vector<int>& nums) {
        int sum = 0;
        std::unordered_map<int, int> freq;
        for (int x : nums) {
            sum += x;
            freq[x]++;
        }
        int ans = INT_MIN;
        for (int x : nums) {
            freq[x]--;
            int rem = sum - x;
            if (rem % 2 == 0) {
                int cand = rem / 2;
                if (freq[cand] > 0 && x > ans) ans = x;
            }
            freq[x]++;
        }
        return ans;
    }
};
