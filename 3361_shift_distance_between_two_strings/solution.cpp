// LeetCode 3361 - Shift Distance Between Two Strings
// https://leetcode.com/problems/shift-distance-between-two-strings/

#include <cstdint>
#include <string>
#include <vector>

class Solution {
public:
    long long shiftDistance(std::string s, std::string t, std::vector<int>& nextCost, std::vector<int>& previousCost) {
        long long ans = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            int a = s[i] - 'a', b = t[i] - 'a';
            if (a == b) continue;
            long long fwd = 0;
            for (int x = a; x != b; x = (x + 1) % 26) fwd += nextCost[x];
            long long bwd = 0;
            for (int x = a; x != b; x = (x + 25) % 26) bwd += previousCost[x];
            ans += fwd < bwd ? fwd : bwd;
        }
        return ans;
    }
};
