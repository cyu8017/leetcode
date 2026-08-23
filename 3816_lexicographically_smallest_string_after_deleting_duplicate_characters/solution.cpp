// LeetCode 3816 - Lexicographically Smallest String After Deleting Duplicate Characters
// https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/

#include <string>
#include <vector>

class Solution {
public:
    std::string lexSmallestAfterDeletion(std::string s) {
        int cnt[26] = {};
        for (char c : s) cnt[c - 'a']++;
        std::string stk;
        for (char c : s) {
            while (!stk.empty() && stk.back() > c && cnt[stk.back() - 'a'] > 1) {
                cnt[stk.back() - 'a']--;
                stk.pop_back();
            }
            stk.push_back(c);
        }
        while (cnt[stk.back() - 'a'] > 1) {
            cnt[stk.back() - 'a']--;
            stk.pop_back();
        }
        return stk;
    }
};
