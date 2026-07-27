// LeetCode 1010 - Pairs of Songs With Total Durations Divisible by 60
// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

#include <vector>

class Solution {
public:
    int numPairsDivisibleBy60(std::vector<int>& time) {
        int count[60] = {};
        int ans = 0;
        for (int t : time) {
            ans += count[(60 - t % 60) % 60];
            count[t % 60]++;
        }
        return ans;
    }
};

