// LeetCode 2433 - Find The Original Array of Prefix Xor
// https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

#include <vector>

class Solution {
public:
    std::vector<int> findArray(std::vector<int>& pref) {
        std::vector<int> ans(pref.size());
        ans[0] = pref[0];
        for (int i = 1; i < (int)pref.size(); i++) {
            ans[i] = pref[i] ^ pref[i - 1];
        }
        return ans;
    }
};
