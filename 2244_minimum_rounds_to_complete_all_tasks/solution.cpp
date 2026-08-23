// LeetCode 2244 - Minimum Rounds to Complete All Tasks
// https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

#include <vector>
#include <unordered_map>

class Solution {
public:
    int minimumRounds(std::vector<int>& tasks) {
        std::unordered_map<int, int> freq;
        for (int t : tasks) freq[t]++;
        int ans = 0;
        for (auto& [_, c] : freq) {
            if (c == 1) return -1;
            ans += (c + 2) / 3;
        }
        return ans;
    }
};
