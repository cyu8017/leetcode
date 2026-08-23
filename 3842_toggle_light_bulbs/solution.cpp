// LeetCode 3842 - Toggle Light Bulbs
// https://leetcode.com/problems/toggle-light-bulbs/

#include <vector>

class Solution {
public:
    std::vector<int> toggleLightBulbs(std::vector<int>& bulbs) {
        int st[101] = {};
        for (int x : bulbs) st[x] ^= 1;
        std::vector<int> ans;
        for (int i = 0; i < 101; i++) if (st[i] == 1) ans.push_back(i);
        return ans;
    }
};
