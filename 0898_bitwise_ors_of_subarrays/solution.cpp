// LeetCode 0898 - Bitwise ORs of Subarrays
// https://leetcode.com/problems/bitwise-ors-of-subarrays/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int subarrayBitwiseORs(std::vector<int>& arr) {
        std::unordered_set<int> ans, cur;
        for (int x : arr) {
            std::unordered_set<int> nxt{x};
            for (int y : cur) {
                nxt.insert(x | y);
            }
            cur.swap(nxt);
            ans.insert(cur.begin(), cur.end());
        }
        return static_cast<int>(ans.size());
    }
};
