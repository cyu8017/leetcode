// LeetCode 1301 - Number of Paths With Max Score
// https://leetcode.com/problems/number-of-paths-with-max-score/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int* pathsWithMaxScore(char** board, int boardSize, int* returnSize) {
    const int MOD = 1000000007;
    int n = boardSize;
    int* score = (int*)malloc(n * n * sizeof(int));
    int* ways = (int*)calloc(n * n, sizeof(int));
    for (int i = 0; i < n * n; i++) score[i] = -1;
    score[(n - 1) * n + (n - 1)] = 0;
    ways[(n - 1) * n + (n - 1)] = 1;
    for (int r = n - 1; r >= 0; r--) {
        for (int c = n - 1; c >= 0; c--) {
            if (board[r][c] == 'X' || (r == n - 1 && c == n - 1)) continue;
            int best = -1, count = 0;
            int dirs[3][2] = {{1, 0}, {0, 1}, {1, 1}};
            for (int d = 0; d < 3; d++) {
                int nr = r + dirs[d][0], nc = c + dirs[d][1];
                if (nr < n && nc < n && score[nr * n + nc] >= 0) {
                    if (score[nr * n + nc] > best) {
                        best = score[nr * n + nc];
                        count = ways[nr * n + nc];
                    } else if (score[nr * n + nc] == best) {
                        count = (count + ways[nr * n + nc]) % MOD;
                    }
                }
            }
            if (best >= 0) {
                int add = isdigit((unsigned char)board[r][c]) ? board[r][c] - '0' : 0;
                score[r * n + c] = best + add;
                ways[r * n + c] = count;
            }
        }
    }
    int* ans = (int*)malloc(2 * sizeof(int));
    ans[0] = score[0] > 0 ? score[0] : 0;
    if (score[0] < 0) ans[0] = 0;
    else ans[0] = score[0];
    ans[1] = ways[0];
    free(score);
    free(ways);
    *returnSize = 2;
    return ans;
}
