// LeetCode 3412 - Find Mirror Score of a String
// https://leetcode.com/problems/find-mirror-score-of-a-string/

#include <cstdint>
#include <string>
#include <vector>

class Solution {
public:
    long long calculateScore(std::string s) {
        std::vector<std::vector<int>> stacks(26);
        long long ans = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            int ci = s[i] - 'a';
            int mir = 25 - ci;
            if (!stacks[mir].empty()) {
                int j = stacks[mir].back();
                stacks[mir].pop_back();
                ans += i - j;
            } else {
                stacks[ci].push_back(i);
            }
        }
        return ans;
    }
};
