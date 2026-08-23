// LeetCode 3226 - Number of Bit Changes to Make Two Integers Equal
// https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/

class Solution {
public:
    int minChanges(int n, int k) {
        if ((n & k) != k) return -1;
        return __builtin_popcount((unsigned)(n ^ k));
    }
};
