// LeetCode 2524 - Maximum Frequency Score of a Subarray
// https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/

#include <unordered_map>
#include <vector>

class Solution {
    static constexpr int MOD = 1000000007;
    long long modPow(long long a, long long e) {
        long long res = 1;
        a %= MOD;
        while (e > 0) {
            if (e & 1) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }
public:
    int maxFrequencyScore(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> freq;
        long long score = 0;
        auto add = [&](int x) {
            int c = freq[x];
            if (c > 0) score = (score - modPow(x, c) + MOD) % MOD;
            freq[x] = c + 1;
            score = (score + modPow(x, c + 1)) % MOD;
        };
        auto remove = [&](int x) {
            int c = freq[x];
            score = (score - modPow(x, c) + MOD) % MOD;
            if (c == 1) freq.erase(x);
            else {
                freq[x] = c - 1;
                score = (score + modPow(x, c - 1)) % MOD;
            }
        };
        long long best = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            add(nums[i]);
            if (i >= k) remove(nums[i - k]);
            if (i >= k - 1 && score > best) best = score;
        }
        return (int)best;
    }
};
