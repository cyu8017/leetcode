// LeetCode 0132 - Palindrome Partitioning II
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    int minCut(string s) {
        int n = s.size();
        vector<vector<bool>> pal(n, vector<bool>(n));
        vector<int> cuts(n);
        for (int i = n - 1; i >= 0; --i)
            for (int j = i; j < n; ++j)
                pal[i][j] = s[i] == s[j] && (j - i < 2 || pal[i + 1][j - 1]);
        for (int i = 0; i < n; ++i) {
            cuts[i] = i;
            for (int j = 0; j <= i; ++j)
                if (pal[j][i]) cuts[i] = j == 0 ? 0 : min(cuts[i], cuts[j - 1] + 1);
        }
        return cuts[n - 1];
    }
};