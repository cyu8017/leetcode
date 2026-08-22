// LeetCode 2018 - Check if Word Can Be Placed In Crossword
// https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

#include <stdbool.h>
#include <string.h>

static bool match2018(char* cells, int L, char* word) {
    bool ok1 = true, ok2 = true;
    for (int i = 0; i < L; i++) {
        if (cells[i] != ' ' && cells[i] != word[i]) ok1 = false;
        if (cells[i] != ' ' && cells[i] != word[L - 1 - i]) ok2 = false;
    }
    return ok1 || ok2;
}

bool placeWordInCrossword(char** board, int boardSize, int* boardColSize, char* word) {
    int m = boardSize, n = boardColSize[0], L = (int)strlen(word);
    char cells[128];
    for (int r = 0; r < m; r++) {
        int c = 0;
        while (c < n) {
            while (c < n && board[r][c] == '#') c++;
            int start = c;
            while (c < n && board[r][c] != '#') c++;
            if (c - start == L) {
                for (int i = 0; i < L; i++) cells[i] = board[r][start + i];
                if (match2018(cells, L, word)) return true;
            }
        }
    }
    for (int c = 0; c < n; c++) {
        int r = 0;
        while (r < m) {
            while (r < m && board[r][c] == '#') r++;
            int start = r;
            while (r < m && board[r][c] != '#') r++;
            if (r - start == L) {
                for (int i = 0; i < L; i++) cells[i] = board[start + i][c];
                if (match2018(cells, L, word)) return true;
            }
        }
    }
    return false;
}
