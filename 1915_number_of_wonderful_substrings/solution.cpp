// LeetCode 1915 - Number of Wonderful Substrings
// https://leetcode.com/problems/number-of-wonderful-substrings/

#include <string>
#include <vector>

class Solution {
public:
    long long wonderfulSubstrings(std::string word) {
        std::vector<long long> count(1024, 0);
        count[0] = 1;
        int mask = 0;
        long long ans = 0;
        for (char ch : word) {
            mask ^= 1 << (ch - 'a');
            ans += count[mask];
            for (int bit = 0; bit < 10; bit++) ans += count[mask ^ (1 << bit)];
            count[mask]++;
        }
        return ans;
    }
};
