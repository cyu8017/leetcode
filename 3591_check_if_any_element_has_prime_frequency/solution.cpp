// LeetCode 3591 - Check if Any Element Has Prime Frequency
// https://leetcode.com/problems/check-if-any-element-has-prime-frequency/

#include <unordered_map>
#include <vector>

class Solution {
    bool isPrime(int x) {
        if (x < 2) return false;
        for (int i = 2; i * i <= x; i++)
            if (x % i == 0) return false;
        return true;
    }

public:
    bool checkPrimeFrequency(std::vector<int>& nums) {
        std::unordered_map<int, int> cnt;
        for (int x : nums) cnt[x]++;
        for (auto& [_, c] : cnt)
            if (isPrime(c)) return true;
        return false;
    }
};
