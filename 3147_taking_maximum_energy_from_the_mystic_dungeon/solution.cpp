// LeetCode 3147 - Taking Maximum Energy From the Mystic Dungeon
// https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maximumEnergy(std::vector<int>& energy, int k) {
        int ans = -(1 << 30);
        int n = (int)energy.size();
        for (int i = n - k; i < n; i++) {
            for (int j = i, s = 0; j >= 0; j -= k) {
                s += energy[j];
                ans = std::max(ans, s);
            }
        }
        return ans;
    }
};
