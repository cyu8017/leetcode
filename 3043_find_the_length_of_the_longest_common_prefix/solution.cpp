// LeetCode 3043 - Find the Length of the Longest Common Prefix
// https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

#include <algorithm>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int longestCommonPrefix(std::vector<int>& arr1, std::vector<int>& arr2) {
        std::unordered_set<int> s;
        for (int x : arr1)
            for (; x > 0; x /= 10) s.insert(x);
        int mx = 0;
        for (int x : arr2) {
            for (; x > 0; x /= 10) {
                if (s.count(x)) {
                    mx = std::max(mx, x);
                    break;
                }
            }
        }
        return mx > 0 ? (int)std::to_string(mx).size() : 0;
    }
};
