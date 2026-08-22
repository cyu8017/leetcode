// LeetCode 2056 - Number of Valid Move Combinations On Chessboard
// https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct { int dr, dc, steps; } Move2056;

static int dirsRook[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
static int dirsBishop[4][2] = {{1,1},{1,-1},{-1,1},{-1,-1}};
static int dirsQueen[8][2] = {{1,0},{-1,0},{0,1},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}};

static int ans2056, n2056;
static Move2056 chosen2056[4];
static Move2056 allMoves2056[4][64];
static int moveCnt2056[4];
static int positions2056[4][2];

static bool okCombo2056(int end) {
    int maxT = 0;
    for (int i = 0; i <= end; i++) if (chosen2056[i].steps > maxT) maxT = chosen2056[i].steps;
    for (int t = 1; t <= maxT; t++) {
        int occupied[9][9];
        memset(occupied, 0, sizeof(occupied));
        for (int i = 0; i <= end; i++) {
            Move2056 m = chosen2056[i];
            int use = m.steps == 0 ? 0 : (t > m.steps ? m.steps : t);
            int pr = positions2056[i][0] + m.dr * use;
            int pc = positions2056[i][1] + m.dc * use;
            if (occupied[pr][pc]) return false;
            occupied[pr][pc] = 1;
        }
    }
    return true;
}

static void dfs2056(int i) {
    if (i == n2056) { ans2056++; return; }
    for (int j = 0; j < moveCnt2056[i]; j++) {
        chosen2056[i] = allMoves2056[i][j];
        if (okCombo2056(i)) dfs2056(i + 1);
    }
}

int countCombinations(char** pieces, int piecesSize, int** positions, int positionsSize, int* positionsColSize) {
    (void)positionsSize; (void)positionsColSize;
    n2056 = piecesSize;
    ans2056 = 0;
    for (int i = 0; i < n2056; i++) {
        positions2056[i][0] = positions[i][0];
        positions2056[i][1] = positions[i][1];
        moveCnt2056[i] = 0;
        allMoves2056[i][moveCnt2056[i]++] = (Move2056){0, 0, 0};
        int (*dirs)[2];
        int dn;
        if (strcmp(pieces[i], "rook") == 0) { dirs = dirsRook; dn = 4; }
        else if (strcmp(pieces[i], "bishop") == 0) { dirs = dirsBishop; dn = 4; }
        else { dirs = dirsQueen; dn = 8; }
        int r = positions[i][0], c = positions[i][1];
        for (int d = 0; d < dn; d++) {
            int nr = r + dirs[d][0], nc = c + dirs[d][1], step = 1;
            while (nr >= 1 && nr <= 8 && nc >= 1 && nc <= 8) {
                allMoves2056[i][moveCnt2056[i]++] = (Move2056){dirs[d][0], dirs[d][1], step};
                nr += dirs[d][0]; nc += dirs[d][1]; step++;
            }
        }
    }
    dfs2056(0);
    return ans2056;
}
