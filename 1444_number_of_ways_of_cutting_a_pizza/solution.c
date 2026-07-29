// LeetCode 1444 - Number of Ways of Cutting a Pizza
// https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

#include <stdlib.h>
#include <string.h>

int ways(char** pizza, int pizzaSize, int k) {
    const int MOD = 1000000007;
    int rows = pizzaSize, cols = (int)strlen(pizza[0]);
    int** apples = (int**)malloc((rows + 1) * sizeof(int*));
    for (int i = 0; i <= rows; i++) apples[i] = (int*)calloc(cols + 1, sizeof(int));
    for (int r = rows - 1; r >= 0; r--)
        for (int c = cols - 1; c >= 0; c--)
            apples[r][c] = (pizza[r][c] == 'A') + apples[r + 1][c] + apples[r][c + 1] - apples[r + 1][c + 1];
    int** dp = (int**)malloc(rows * sizeof(int*));
    for (int r = 0; r < rows; r++) {
        dp[r] = (int*)malloc(cols * sizeof(int));
        for (int c = 0; c < cols; c++) dp[r][c] = apples[r][c] ? 1 : 0;
    }
    for (int cut = 1; cut < k; cut++) {
        int** nxt = (int**)malloc(rows * sizeof(int*));
        for (int r = 0; r < rows; r++) {
            nxt[r] = (int*)calloc(cols, sizeof(int));
            for (int c = 0; c < cols; c++) {
                long long ways_sum = 0;
                for (int nr = r + 1; nr < rows; nr++)
                    if (apples[r][c] > apples[nr][c]) ways_sum += dp[nr][c];
                for (int nc = c + 1; nc < cols; nc++)
                    if (apples[r][c] > apples[r][nc]) ways_sum += dp[r][nc];
                nxt[r][c] = (int)(ways_sum % MOD);
            }
        }
        for (int r = 0; r < rows; r++) free(dp[r]);
        free(dp); dp = nxt;
    }
    int ans = dp[0][0];
    for (int r = 0; r < rows; r++) free(dp[r]);
    free(dp);
    for (int i = 0; i <= rows; i++) free(apples[i]);
    free(apples);
    return ans;
}
