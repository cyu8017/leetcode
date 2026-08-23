// LeetCode 2937 - Make Three Strings Equal
// https://leetcode.com/problems/make-three-strings-equal/

#include <algorithm>
#include <string>

class Solution {
public:
    int findMinimumOperations(std::string s1, std::string s2, std::string s3) {
        int n = (int)std::min({s1.size(), s2.size(), s3.size()});
        int i = 0;
        while (i < n && s1[i] == s2[i] && s2[i] == s3[i]) i++;
        if (i == 0) return -1;
        return (int)s1.size() + (int)s2.size() + (int)s3.size() - 3 * i;
    }
};
