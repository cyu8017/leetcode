// LeetCode 2562 - Find the Array Concatenation Value
// https://leetcode.com/problems/find-the-array-concatenation-value/

#include <vector>

class Solution {
public:
    long long findTheArrayConcVal(std::vector<int>& nums) {
        long long ans = 0;
        int l = 0, r = (int)nums.size() - 1;
        while (l <= r) {
            if (l == r) {
                ans += nums[l];
                break;
            }
            int left = nums[l], right = nums[r];
            long long pow = 1;
            for (int t = right; t > 0; t /= 10) pow *= 10;
            ans += (long long)left * pow + right;
            l++;
            r--;
        }
        return ans;
    }
};
