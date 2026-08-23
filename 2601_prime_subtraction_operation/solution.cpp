// LeetCode 2601 - Prime Subtraction Operation
// https://leetcode.com/problems/prime-subtraction-operation/

#include <algorithm>
#include <vector>

class Solution {
public:
    bool primeSubOperation(std::vector<int>& nums) {
        int maxV = *std::max_element(nums.begin(), nums.end());
        std::vector<char> isP(maxV + 1, true);
        if (maxV >= 0) isP[0] = false;
        if (maxV >= 1) isP[1] = false;
        for (int i = 2; i * i <= maxV; ++i) {
            if (isP[i]) {
                for (int j = i * i; j <= maxV; j += i) isP[j] = false;
            }
        }
        std::vector<int> primes;
        for (int i = 2; i <= maxV; ++i) if (isP[i]) primes.push_back(i);
        int prev = 0;
        for (int x : nums) {
            if (x <= prev) return false;
            int best = x;
            for (int p : primes) {
                if (p >= x) break;
                if (x - p > prev) best = x - p;
            }
            prev = best;
        }
        return true;
    }
};
