// LeetCode 1222 - Queens That Can Attack the King
// https://leetcode.com/problems/queens-that-can-attack-the-king/

#include <stdlib.h>
#include <string.h>

static int occupied[8][8];

int** queensAttacktheKing(int** queens, int queensSize, int* queensColSize, int* king, int kingSize, int* returnSize, int** returnColumnSizes) {
    (void)queensColSize;
    (void)kingSize;
    memset(occupied, 0, sizeof(occupied));
    for (int i = 0; i < queensSize; i++) occupied[queens[i][0]][queens[i][1]] = 1;
    int** answer = (int**)malloc(8 * sizeof(int*));
    int count = 0;
    const int dirs[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
    for (int d = 0; d < 8; d++) {
        int r = king[0] + dirs[d][0];
        int c = king[1] + dirs[d][1];
        while (r >= 0 && r < 8 && c >= 0 && c < 8) {
            if (occupied[r][c]) {
                answer[count] = (int*)malloc(2 * sizeof(int));
                answer[count][0] = r;
                answer[count][1] = c;
                count++;
                break;
            }
            r += dirs[d][0];
            c += dirs[d][1];
        }
    }
    *returnSize = count;
    *returnColumnSizes = (int*)malloc((size_t)count * sizeof(int));
    for (int i = 0; i < count; i++) (*returnColumnSizes)[i] = 2;
    return answer;
}
