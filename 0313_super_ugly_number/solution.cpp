// LeetCode 0313 - Super Ugly Number
// https://leetcode.com/problems/super-ugly-number/

#include <algorithm>
#include <vector>

class Solution {
public:
    int nthSuperUglyNumber(int n, std::vector<int>& primes) {
        std::vector<int> ugly = {1};
        std::vector<int> pointers(primes.size(), 0);

        while (static_cast<int>(ugly.size()) < n) {
            std::vector<long long> nextValues;
            nextValues.reserve(primes.size());
            for (size_t index = 0; index < primes.size(); index++) {
                nextValues.push_back(1LL * ugly[pointers[index]] * primes[index]);
            }
            long long nextUgly = *std::min_element(nextValues.begin(), nextValues.end());
            ugly.push_back(static_cast<int>(nextUgly));
            for (size_t index = 0; index < primes.size(); index++) {
                if (nextUgly == 1LL * ugly[pointers[index]] * primes[index]) {
                    pointers[index] += 1;
                }
            }
        }

        return ugly.back();
    }
};
