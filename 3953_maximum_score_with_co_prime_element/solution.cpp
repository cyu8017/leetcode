// LeetCode 3953 - Maximum Score with Co-Prime Element
// https://leetcode.com/problems/maximum-score-with-co-prime-element/

#include <vector>

class Solution {
public:
    int maxScore(std::vector<int>& nums, int maxVal) {
        int limit = maxVal;
        std::vector<int> frequency(100001, 0);
        for (int x : nums) {
            frequency[x]++;
            if (x > limit) limit = x;
        }
        std::vector<int> divisible(limit + 1, 0);
        for (int d = 1; d <= limit; d++) {
            for (int multiple = d; multiple <= limit; multiple += d) {
                if (multiple < (int)frequency.size()) divisible[d] += frequency[multiple];
            }
        }
        auto badCount = [&](int x) {
            std::vector<int> primes;
            int y = x;
            for (int p = 2; 1LL * p * p <= y; p++) {
                if (y % p == 0) {
                    primes.push_back(p);
                    while (y % p == 0) y /= p;
                }
            }
            if (y > 1) primes.push_back(y);
            int bad = 0;
            int psz = (int)primes.size();
            for (int mask = 1; mask < (1 << psz); mask++) {
                int product = 1, bits = 0;
                for (int i = 0; i < psz; i++) {
                    if ((mask >> i) & 1) {
                        product *= primes[i];
                        bits++;
                    }
                }
                if (bits % 2 == 1) bad += divisible[product];
                else bad -= divisible[product];
            }
            return bad;
        };
        int best = -(int)nums.size();
        std::vector<bool> checked(limit + 1, false);
        auto evaluate = [&](int x, bool exists) {
            if (checked[x]) return;
            checked[x] = true;
            int bad = badCount(x);
            int cost = 0;
            if (exists) {
                if (x > 1) cost = bad - 1;
            } else if (bad > 0) cost = bad;
            else cost = 1;
            if (x - cost > best) best = x - cost;
        };
        for (int x = 1; x <= maxVal; x++) {
            evaluate(x, x < (int)frequency.size() && frequency[x] > 0);
        }
        for (int x : nums) evaluate(x, true);
        return best;
    }
};
