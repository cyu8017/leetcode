// LeetCode 3272 - Find the Count of Good Integers
// https://leetcode.com/problems/find-the-count-of-good-integers/

#include <algorithm>
#include <cstdint>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
    std::string itoa(int x) {
        if (x == 0) return "0";
        std::string b;
        while (x > 0) {
            b.insert(b.begin(), char('0' + x % 10));
            x /= 10;
        }
        return b;
    }

    int atoiStr(const std::string& s) {
        int v = 0;
        for (char c : s) v = v * 10 + (c - '0');
        return v;
    }

public:
    long long countGoodIntegers(int n, int k) {
        int half = (n + 1) / 2;
        int start = 1;
        for (int i = 1; i < half; i++) start *= 10;
        int end = start * 10;
        std::unordered_set<std::string> seen;
        int64_t ans = 0;
        std::vector<int64_t> fact(n + 1);
        fact[0] = 1;
        for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i;
        for (int h = start; h < end; h++) {
            std::string s = itoa(h);
            std::string pal = s;
            int revStart = (int)s.size() - 1;
            if (n % 2 == 1) revStart--;
            for (int i = revStart; i >= 0; i--) pal += s[i];
            if (atoiStr(pal) % k != 0) continue;
            std::string chars = pal;
            std::sort(chars.begin(), chars.end());
            if (seen.count(chars)) continue;
            seen.insert(chars);
            int cnt[10] = {};
            for (char c : chars) cnt[c - '0']++;
            int64_t total = fact[n];
            for (int c : cnt) total /= fact[c];
            if (cnt[0] > 0) {
                int64_t bad = fact[n - 1];
                cnt[0]--;
                for (int c : cnt) bad /= fact[c];
                cnt[0]++;
                total -= bad;
            }
            ans += total;
        }
        return ans;
    }
};
