// LeetCode 2744 - Find Maximum Number of String Pairs
// https://leetcode.com/problems/find-maximum-number-of-string-pairs/

#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int maximumNumberOfStringPairs(std::vector<std::string>& words) {
        std::unordered_map<std::string, int> freq;
        int ans = 0;
        for (auto& w : words) {
            std::string rev = w;
            std::reverse(rev.begin(), rev.end());
            if (freq[rev] > 0) { ans++; freq[rev]--; }
            else freq[w]++;
        }
        return ans;
    }
};
