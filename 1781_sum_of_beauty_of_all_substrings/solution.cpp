// LeetCode 1781 - Sum of Beauty of All Substrings
// https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

#include <algorithm>
#include <climits>
#include <string>

class Solution {
public:
    int beautySum(std::string s) {
        int ans = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            int freq[26] = {0};
            for (int j = i; j < (int)s.size(); j++) {
                freq[s[j] - 'a']++;
                int lo = INT_MAX;
                int hi = 0;
                for (int count : freq) {
                    if (count > 0) {
                        lo = std::min(lo, count);
                        hi = std::max(hi, count);
                    }
                }
                ans += hi - lo;
            }
        }
        return ans;
    }
};
