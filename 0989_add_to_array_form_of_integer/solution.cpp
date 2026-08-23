// LeetCode 0989 - Add to Array-Form of Integer
// https://leetcode.com/problems/add-to-array-form-of-integer/

#include <vector>

class Solution {
public:
    std::vector<int> addToArrayForm(std::vector<int>& num, int k) {
        int i = (int)num.size() - 1;
        while (k || i >= 0) {
            if (i >= 0) {
                k += num[i];
                num[i] = k % 10;
                i--;
            } else {
                num.insert(num.begin(), k % 10);
            }
            k /= 10;
        }
        return num;
    }
};
