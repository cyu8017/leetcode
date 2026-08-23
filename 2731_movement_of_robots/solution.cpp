// LeetCode 2731 - Movement of Robots
// https://leetcode.com/problems/movement-of-robots/

#include <vector>
#include <string>
#include <algorithm>

class Solution {
public:
    int sumDistance(std::vector<int>& nums, std::string s, int d) {
        const int MOD = 1000000007;
        int n = (int)nums.size();
        std::vector<long long> pos(n);
        for (int i = 0; i < n; i++)
            pos[i] = nums[i] + (s[i] == 'R' ? d : -d);
        std::sort(pos.begin(), pos.end());
        long long ans = 0, pref = 0;
        for (int i = 0; i < n; i++) {
            ans = (ans + pos[i] * i - pref) % MOD;
            pref += pos[i];
        }
        return (int)((ans % MOD + MOD) % MOD);
    }
};
