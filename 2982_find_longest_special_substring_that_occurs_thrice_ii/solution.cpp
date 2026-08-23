// LeetCode 2982 - Find Longest Special Substring That Occurs Thrice II
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

#include <string>
#include <vector>
#include <algorithm>
#include <functional>

class Solution {
public:
    int maximumLength(std::string s) {
        std::vector<int> groups[26];
        int n = (int)s.size();
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && s[j] == s[i]) j++;
            groups[s[i] - 'a'].push_back(j - i);
            i = j;
        }
        int ans = -1;
        for (int c = 0; c < 26; c++) {
            auto& arr = groups[c];
            if (arr.empty()) continue;
            std::sort(arr.begin(), arr.end(), std::greater<int>());
            for (int L = arr[0]; L >= 1; L--) {
                int cnt = 0;
                for (int g : arr) {
                    if (g >= L) cnt += g - L + 1;
                }
                if (cnt >= 3) {
                    if (L > ans) ans = L;
                    break;
                }
            }
        }
        return ans;
    }
};
