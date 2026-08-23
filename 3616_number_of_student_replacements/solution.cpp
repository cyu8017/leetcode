// LeetCode 3616 - Number of Student Replacements
// https://leetcode.com/problems/number-of-student-replacements/

#include <vector>

class Solution {
public:
    int totalReplacements(std::vector<int>& ranks) {
        int ans = 0, cur = ranks[0];
        for (int x : ranks) {
            if (x < cur) {
                cur = x;
                ans++;
            }
        }
        return ans;
    }
};
