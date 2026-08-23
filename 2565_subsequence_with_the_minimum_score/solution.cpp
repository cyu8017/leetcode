// LeetCode 2565 - Subsequence With the Minimum Score
// https://leetcode.com/problems/subsequence-with-the-minimum-score/

#include <string>
#include <vector>

class Solution {
public:
    int minimumScore(std::string s, std::string t) {
        int n = (int)s.size(), m = (int)t.size();
        std::vector<int> left(m, -1), right(m, -1);
        int j = 0;
        for (int i = 0; i < n && j < m; ++i) {
            if (s[i] == t[j]) {
                left[j] = i;
                j++;
            }
        }
        j = m - 1;
        for (int i = n - 1; i >= 0 && j >= 0; --i) {
            if (s[i] == t[j]) {
                right[j] = i;
                j--;
            }
        }
        if (left[m - 1] != -1) return 0;
        int ans = m;
        for (int i = 0; i < m; ++i) {
            if (right[i] != -1) {
                if (i < ans) ans = i;
                break;
            }
        }
        for (int i = m - 1; i >= 0; --i) {
            if (left[i] != -1) {
                if (m - 1 - i < ans) ans = m - 1 - i;
                break;
            }
        }
        j = 0;
        for (int i = 0; i < m; ++i) {
            if (left[i] == -1) break;
            while (j < m && (right[j] == -1 || right[j] <= left[i])) j++;
            if (j < m) {
                int rem = j - i - 1;
                if (rem < ans) ans = rem;
            }
        }
        return ans;
    }
};
