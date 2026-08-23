// LeetCode 3167 - Better Compression of String
// https://leetcode.com/problems/better-compression-of-string/

#include <string>
#include <unordered_map>

class Solution {
public:
    std::string betterCompression(std::string compressed) {
        std::unordered_map<char, int> cnt;
        int n = (int)compressed.size();
        for (int i = 0; i < n; ) {
            char c = compressed[i];
            int j = i + 1, x = 0;
            while (j < n && compressed[j] >= '0' && compressed[j] <= '9') {
                x = x * 10 + (compressed[j] - '0');
                j++;
            }
            cnt[c] += x;
            i = j;
        }
        std::string ans;
        for (char c = 'a'; c <= 'z'; c++) {
            if (cnt[c] > 0) {
                ans.push_back(c);
                ans += std::to_string(cnt[c]);
            }
        }
        return ans;
    }
};
