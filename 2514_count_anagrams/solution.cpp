// LeetCode 2514 - Count Anagrams
// https://leetcode.com/problems/count-anagrams/

#include <sstream>
#include <string>
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
    int countAnagrams(std::string s) {
        std::istringstream iss(s);
        std::vector<std::string> words;
        std::string w;
        int maxN = 0;
        while (iss >> w) {
            words.push_back(w);
            if ((int)w.size() > maxN) maxN = (int)w.size();
        }
        std::vector<long long> fact(maxN + 1), invFact(maxN + 1);
        fact[0] = 1;
        for (int i = 1; i <= maxN; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[maxN] = modPow(fact[maxN], MOD - 2);
        for (int i = maxN; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;
        long long ans = 1;
        for (auto& word : words) {
            int cnt[26] = {};
            for (char c : word) cnt[c - 'a']++;
            long long cur = fact[(int)word.size()];
            for (int c : cnt) cur = cur * invFact[c] % MOD;
            ans = ans * cur % MOD;
        }
        return (int)ans;
    }
};
