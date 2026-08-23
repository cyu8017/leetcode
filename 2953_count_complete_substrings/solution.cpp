// LeetCode 2953 - Count Complete Substrings
// https://leetcode.com/problems/count-complete-substrings/

#include <cstdlib>
#include <string>

class Solution {
public:
    int countCompleteSubstrings(std::string word, int k) {
        int n = (int)word.size(), ans = 0;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j + 1 < n && std::abs((int)word[j + 1] - (int)word[j]) <= 2) j++;
            std::string seg = word.substr(i, j - i + 1);
            int m = (int)seg.size();
            for (int chars = 1; chars <= 26; chars++) {
                int length = chars * k;
                if (length > m) break;
                int freq[26] = {};
                int unique = 0;
                for (int r = 0; r < m; r++) {
                    int c = seg[r] - 'a';
                    freq[c]++;
                    if (freq[c] == 1) unique++;
                    if (r >= length) {
                        int c2 = seg[r - length] - 'a';
                        freq[c2]--;
                        if (freq[c2] == 0) unique--;
                    }
                    if (r >= length - 1 && unique == chars) {
                        bool ok = true;
                        for (int f : freq)
                            if (f != 0 && f != k) { ok = false; break; }
                        if (ok) ans++;
                    }
                }
            }
            i = j + 1;
        }
        return ans;
    }
};
