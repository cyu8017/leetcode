// LeetCode 3287 - Find the Maximum Sequence Value of Array
// https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/

#include <vector>

class Solution {
public:
    int maxValue(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        const int MAX = 128;
        std::vector<std::vector<std::vector<char>>> left(n + 1, std::vector<std::vector<char>>(k + 1, std::vector<char>(MAX, 0)));
        left[0][0][0] = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= k; j++) {
                for (int v = 0; v < MAX; v++) {
                    if (!left[i][j][v]) continue;
                    left[i + 1][j][v] = 1;
                    if (j < k) left[i + 1][j + 1][v | nums[i]] = 1;
                }
            }
        }
        std::vector<std::vector<std::vector<char>>> right(n + 1, std::vector<std::vector<char>>(k + 1, std::vector<char>(MAX, 0)));
        right[n][0][0] = 1;
        for (int i = n - 1; i >= 0; i--) {
            for (int j = 0; j <= k; j++) {
                for (int v = 0; v < MAX; v++) {
                    if (!right[i + 1][j][v]) continue;
                    right[i][j][v] = 1;
                    if (j < k) right[i][j + 1][v | nums[i]] = 1;
                }
            }
        }
        int ans = 0;
        for (int mid = k; mid + k <= n; mid++) {
            for (int a = 0; a < MAX; a++) {
                if (!left[mid][k][a]) continue;
                for (int b = 0; b < MAX; b++) {
                    if (right[mid][k][b] && (a ^ b) > ans) ans = a ^ b;
                }
            }
        }
        return ans;
    }
};
