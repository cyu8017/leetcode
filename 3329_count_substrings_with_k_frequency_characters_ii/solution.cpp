// LeetCode 3329 - Count Substrings With K-Frequency Characters II
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/

#include <array>
#include <string>

class Solution {
public:
    long long numberOfSubstrings(std::string s, int k) {
        int n = (int)s.size();
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            std::array<int, 26> freq{};
            for (int j = i; j < n; j++) {
                freq[s[j] - 'a']++;
                bool ok = false;
                for (int f : freq) if (f >= k) { ok = true; break; }
                if (ok) { ans += n - j; break; }
            }
        }
        return ans;
    }
};
