// LeetCode 1728 - Cat and Mouse II
// https://leetcode.com/problems/cat-and-mouse-ii/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int rows;
    int cols;
    int cells;
    int food;
    int maxTurn;
    int** mouseMoves;
    int* mouseMoveCounts;
    int** catMoves;
    int* catMoveCounts;
    signed char* memo;
} GameContext;

static int* computeMoves(char** grid, GameContext* ctx, int pos, int jump, int* outCount) {
    int r = pos / ctx->cols;
    int c = pos % ctx->cols;
    int* out = (int*)malloc((1 + 4 * jump) * sizeof(int));
    int size = 0;
    out[size++] = pos;
    const int dirs[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    for (int d = 0; d < 4; d++) {
        for (int step = 1; step <= jump; step++) {
            int nr = r + dirs[d][0] * step;
            int nc = c + dirs[d][1] * step;
            if (nr < 0 || nr >= ctx->rows || nc < 0 || nc >= ctx->cols || grid[nr][nc] == '#') break;
            out[size++] = nr * ctx->cols + nc;
        }
    }
    *outCount = size;
    return out;
}

static bool win(GameContext* ctx, int m, int c, int turn) {
    if (turn >= ctx->maxTurn) return false;
    if (m == ctx->food) return true;
    if (c == ctx->food || c == m) return false;
    int key = (m * ctx->cells + c) * ctx->maxTurn + turn;
    if (ctx->memo[key] != 0) return ctx->memo[key] == 1;
    bool result;
    if (turn % 2 == 0) {
        result = false;
        for (int i = 0; i < ctx->mouseMoveCounts[m]; i++) {
            if (win(ctx, ctx->mouseMoves[m][i], c, turn + 1)) {
                result = true;
                break;
            }
        }
    } else {
        result = true;
        for (int i = 0; i < ctx->catMoveCounts[c]; i++) {
            if (!win(ctx, m, ctx->catMoves[c][i], turn + 1)) {
                result = false;
                break;
            }
        }
    }
    ctx->memo[key] = result ? 1 : 2;
    return result;
}

bool canMouseWin(char** grid, int gridSize, int catJump, int mouseJump) {
    GameContext ctx;
    ctx.rows = gridSize;
    ctx.cols = (int)strlen(grid[0]);
    ctx.cells = ctx.rows * ctx.cols;
    int totalOpen = 0;
    int mouse = 0;
    int cat = 0;
    ctx.food = 0;
    for (int r = 0; r < ctx.rows; r++) {
        for (int c = 0; c < ctx.cols; c++) {
            char cell = grid[r][c];
            if (cell != '#') totalOpen++;
            if (cell == 'M') mouse = r * ctx.cols + c;
            else if (cell == 'C') cat = r * ctx.cols + c;
            else if (cell == 'F') ctx.food = r * ctx.cols + c;
        }
    }
    ctx.mouseMoves = (int**)calloc(ctx.cells, sizeof(int*));
    ctx.mouseMoveCounts = (int*)calloc(ctx.cells, sizeof(int));
    ctx.catMoves = (int**)calloc(ctx.cells, sizeof(int*));
    ctx.catMoveCounts = (int*)calloc(ctx.cells, sizeof(int));
    for (int r = 0; r < ctx.rows; r++) {
        for (int c = 0; c < ctx.cols; c++) {
            if (grid[r][c] != '#') {
                int pos = r * ctx.cols + c;
                ctx.mouseMoves[pos] = computeMoves(grid, &ctx, pos, mouseJump, &ctx.mouseMoveCounts[pos]);
                ctx.catMoves[pos] = computeMoves(grid, &ctx, pos, catJump, &ctx.catMoveCounts[pos]);
            }
        }
    }
    ctx.maxTurn = 2 * totalOpen;
    ctx.memo = (signed char*)calloc((size_t)ctx.cells * ctx.cells * ctx.maxTurn, sizeof(signed char));
    bool result = win(&ctx, mouse, cat, 0);
    for (int pos = 0; pos < ctx.cells; pos++) {
        free(ctx.mouseMoves[pos]);
        free(ctx.catMoves[pos]);
    }
    free(ctx.mouseMoves);
    free(ctx.mouseMoveCounts);
    free(ctx.catMoves);
    free(ctx.catMoveCounts);
    free(ctx.memo);
    return result;
}
