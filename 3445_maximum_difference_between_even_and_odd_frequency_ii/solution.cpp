// LeetCode 3445 - Maximum Difference Between Even and Odd Frequency II
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/

#include <string>
#include <vector>

class Solution {
public:
    int maxDifference(std::string s, int k) {
        int n = (int)s.size();
        int ans = -1000000000;
        for (int a = 0; a < 5; a++) {
            for (int b = 0; b < 5; b++) {
                if (a == b) continue;
                std::vector<int> prefA(n + 1), prefB(n + 1);
                for (int i = 0; i < n; i++) {
                    prefA[i + 1] = prefA[i];
                    prefB[i + 1] = prefB[i];
                    if (s[i] - '0' == a) prefA[i + 1]++;
                    if (s[i] - '0' == b) prefB[i + 1]++;
                }
                for (int i = 0; i < n; i++) {
                    for (int j = i + k - 1; j < n; j++) {
                        int fa = prefA[j + 1] - prefA[i];
                        int fb = prefB[j + 1] - prefB[i];
                        if (fa % 2 == 1 && fb % 2 == 0 && fb > 0) {
                            if (fa - fb > ans) ans = fa - fb;
                        }
                    }
                }
            }
        }
        return ans;
    }
};
