// LeetCode 0913 - Cat and Mouse
// https://leetcode.com/problems/cat-and-mouse/

#include <stdlib.h>
#include <string.h>

int catMouseGame(int** graph, int graphSize, int* graphColSize) {
    int n = graphSize;
    int DRAW = 0, MOUSE_WIN = 1, CAT_WIN = 2;
    int*** states = (int***)malloc((size_t)n * sizeof(int**));
    int*** out_degree = (int***)malloc((size_t)n * sizeof(int**));
    for (int c = 0; c < n; c++) {
        states[c] = (int**)malloc((size_t)n * sizeof(int*));
        out_degree[c] = (int**)malloc((size_t)n * sizeof(int*));
        for (int m = 0; m < n; m++) {
            states[c][m] = (int*)calloc(2, sizeof(int));
            out_degree[c][m] = (int*)calloc(2, sizeof(int));
            out_degree[c][m][0] = graphColSize[m];
            int catOut = 0;
            for (int i = 0; i < graphColSize[c]; i++) if (graph[c][i] != 0) catOut++;
            out_degree[c][m][1] = catOut;
        }
    }
    int *qc = malloc(n * n * 2 * sizeof(int));
    int *qm = malloc(n * n * 2 * sizeof(int));
    int *qmv = malloc(n * n * 2 * sizeof(int));
    int *qs = malloc(n * n * 2 * sizeof(int));
    int head = 0, tail = 0;
    for (int cat = 1; cat < n; cat++) {
        for (int move = 0; move < 2; move++) {
            states[cat][0][move] = MOUSE_WIN;
            qc[tail]=cat; qm[tail]=0; qmv[tail]=move; qs[tail]=MOUSE_WIN; tail++;
            states[cat][cat][move] = CAT_WIN;
            qc[tail]=cat; qm[tail]=cat; qmv[tail]=move; qs[tail]=CAT_WIN; tail++;
        }
    }
    while (head < tail) {
        int cat = qc[head], mouse = qm[head], move = qmv[head], state = qs[head];
        head++;
        if (cat == 2 && mouse == 1 && move == 0) {
            int ans = state;
            for (int c=0;c<n;c++){for(int m=0;m<n;m++){free(states[c][m]);free(out_degree[c][m]);}free(states[c]);free(out_degree[c]);}
            free(states);free(out_degree);free(qc);free(qm);free(qmv);free(qs);
            return ans;
        }
        int prev_move = move ^ 1;
        int* nodes = prev_move ? graph[cat] : graph[mouse];
        int nsz = prev_move ? graphColSize[cat] : graphColSize[mouse];
        for (int i = 0; i < nsz; i++) {
            int prev = nodes[i];
            int prev_cat = prev_move ? prev : cat;
            if (prev_cat == 0) continue;
            int prev_mouse = prev_move ? mouse : prev;
            if (states[prev_cat][prev_mouse][prev_move]) continue;
            if ((prev_move == 0 && state == MOUSE_WIN) || (prev_move == 1 && state == CAT_WIN) ||
                out_degree[prev_cat][prev_mouse][prev_move] == 1) {
                states[prev_cat][prev_mouse][prev_move] = state;
                qc[tail]=prev_cat; qm[tail]=prev_mouse; qmv[tail]=prev_move; qs[tail]=state; tail++;
            } else {
                out_degree[prev_cat][prev_mouse][prev_move]--;
            }
        }
    }
    int ans = states[2][1][0];
    for (int c=0;c<n;c++){for(int m=0;m<n;m++){free(states[c][m]);free(out_degree[c][m]);}free(states[c]);free(out_degree[c]);}
    free(states);free(out_degree);free(qc);free(qm);free(qmv);free(qs);
    return ans;
}
