// LeetCode 3706 - Maximum Distance Between Unequal Words in Array II
// https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-ii/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    int maxDistance(std::vector<std::string>& words) {
        int n = (int)words.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            if (words[i] != words[0]) ans = std::max(ans, i + 1);
            if (words[i] != words[n - 1]) ans = std::max(ans, n - i);
        }
        return ans;
    }
};
