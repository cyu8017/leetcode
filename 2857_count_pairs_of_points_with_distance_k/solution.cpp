// LeetCode 2857 - Count Pairs of Points With Distance k
// https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

#include <map>
#include <vector>

class Solution {
public:
    int countPairs(std::vector<std::vector<int>>& coordinates, int k) {
        std::map<std::pair<int, int>, int> freq;
        int ans = 0;
        for (auto& p : coordinates) {
            int x = p[0], y = p[1];
            for (int a = 0; a <= k; a++) {
                int b = k - a;
                ans += freq[{x ^ a, y ^ b}];
            }
            freq[{x, y}]++;
        }
        return ans;
    }
};
