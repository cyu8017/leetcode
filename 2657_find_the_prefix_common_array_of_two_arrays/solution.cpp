// LeetCode 2657 - Find the Prefix Common Array of Two Arrays
// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

#include <vector>

class Solution {
public:
    std::vector<int> findThePrefixCommonArray(std::vector<int>& A, std::vector<int>& B) {
        int n = (int)A.size();
        std::vector<char> seenA(n + 1), seenB(n + 1);
        std::vector<int> ans(n);
        int common = 0;
        for (int i = 0; i < n; i++) {
            if (seenB[A[i]]) common++;
            seenA[A[i]] = 1;
            if (seenA[B[i]]) common++;
            seenB[B[i]] = 1;
            ans[i] = common;
        }
        return ans;
    }
};
