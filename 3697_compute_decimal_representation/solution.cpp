// LeetCode 3697 - Compute Decimal Representation
// https://leetcode.com/problems/compute-decimal-representation/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> decimalRepresentation(int n) {
        std::vector<int> ans;
        int p = 1;
        while (n > 0) {
            int v = n % 10;
            n /= 10;
            if (v != 0) ans.push_back(p * v);
            p *= 10;
        }
        std::reverse(ans.begin(), ans.end());
        return ans;
    }
};
