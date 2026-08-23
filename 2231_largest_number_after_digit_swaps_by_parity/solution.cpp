// LeetCode 2231 - Largest Number After Digit Swaps by Parity
// https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

#include <vector>
#include <algorithm>

class Solution {
public:
    int largestInteger(int num) {
        std::vector<int> digits;
        for (int x = num; x > 0; x /= 10) digits.insert(digits.begin(), x % 10);
        std::vector<int> even, odd;
        for (int d : digits) {
            if (d % 2 == 0) even.push_back(d);
            else odd.push_back(d);
        }
        std::sort(even.rbegin(), even.rend());
        std::sort(odd.rbegin(), odd.rend());
        int ei = 0, oi = 0, ans = 0;
        for (int d : digits) {
            if (d % 2 == 0) ans = ans * 10 + even[ei++];
            else ans = ans * 10 + odd[oi++];
        }
        return ans;
    }
};
