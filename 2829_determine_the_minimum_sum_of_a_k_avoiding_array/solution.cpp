// LeetCode 2829 - Determine the Minimum Sum of a k-avoiding Array
// https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

#include <unordered_set>

class Solution {
public:
    int minimumSum(int n, int k) {
        std::unordered_set<int> used;
        int sum = 0, x = 1;
        while ((int)used.size() < n) {
            if (!used.count(k - x)) {
                used.insert(x);
                sum += x;
            }
            x++;
        }
        return sum;
    }
};
