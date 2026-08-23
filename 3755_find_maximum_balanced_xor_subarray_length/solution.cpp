// LeetCode 3755 - Find Maximum Balanced Xor Subarray Length
// https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int maxBalancedSubarray(std::vector<int>& nums) {
        std::unordered_map<long long, int> d;
        int a = 0, b = (int)nums.size(), ans = 0;
        d[b] = -1;
        for (int i = 0; i < (int)nums.size(); i++) {
            a ^= nums[i];
            if (nums[i] % 2 == 0) b++;
            else b--;
            long long key = ((long long)a << 32) | (long long)b;
            auto it = d.find(key);
            if (it != d.end()) ans = std::max(ans, i - it->second);
            else d[key] = i;
        }
        return ans;
    }
};
