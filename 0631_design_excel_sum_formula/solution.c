// LeetCode 0631 - Design Excel Sum Formula
// https://leetcode.com/problems/design-excel-sum-formula/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int r, c;
} Cell;

typedef struct {
    int height;
    int width;
    int values[30][26];
    Cell* formulas[30][26];
    int formulaSizes[30][26];
} Excel;

static void parseCell(const char* cell, int* r, int* c) {
    *c = cell[0] - 'A';
    *r = atoi(cell + 1);
}

static int evalCell(Excel* obj, int row, int col);

Excel* excelCreate(int height, char width) {
    Excel* obj = (Excel*)calloc(1, sizeof(Excel));
    obj->height = height;
    obj->width = width - 'A' + 1;
    return obj;
}

void excelSet(Excel* obj, int row, char column, int val) {
    int col = column - 'A';
    free(obj->formulas[row][col]);
    obj->formulas[row][col] = NULL;
    obj->formulaSizes[row][col] = 0;
    obj->values[row][col] = val;
}

static int evalCell(Excel* obj, int row, int col) {
    if (obj->formulas[row][col]) {
        int sum = 0;
        for (int i = 0; i < obj->formulaSizes[row][col]; i++) {
            sum += evalCell(obj, obj->formulas[row][col][i].r, obj->formulas[row][col][i].c);
        }
        return sum;
    }
    return obj->values[row][col];
}

int excelGet(Excel* obj, int row, char column) {
    return evalCell(obj, row, column - 'A');
}

int excelSum(Excel* obj, int row, char column, char** numbers, int numbersSize) {
    int col = column - 'A';
    Cell* cells = NULL;
    int count = 0, cap = 0;
    for (int t = 0; t < numbersSize; t++) {
        char* token = numbers[t];
        char* colon = strchr(token, ':');
        if (colon) {
            char start[16], end[16];
            int len = (int)(colon - token);
            memcpy(start, token, (size_t)len); start[len] = '\0';
            strcpy(end, colon + 1);
            int r1, c1, r2, c2;
            parseCell(start, &r1, &c1);
            parseCell(end, &r2, &c2);
            for (int r = r1; r <= r2; r++) for (int c = c1; c <= c2; c++) {
                if (count == cap) { cap = cap ? cap * 2 : 8; cells = (Cell*)realloc(cells, (size_t)cap * sizeof(Cell)); }
                cells[count].r = r; cells[count].c = c; count++;
            }
        } else {
            int r, c; parseCell(token, &r, &c);
            if (count == cap) { cap = cap ? cap * 2 : 8; cells = (Cell*)realloc(cells, (size_t)cap * sizeof(Cell)); }
            cells[count].r = r; cells[count].c = c; count++;
        }
    }
    free(obj->formulas[row][col]);
    obj->formulas[row][col] = cells;
    obj->formulaSizes[row][col] = count;
    return evalCell(obj, row, col);
}

void excelFree(Excel* obj) {
    for (int r = 0; r < 30; r++) for (int c = 0; c < 26; c++) free(obj->formulas[r][c]);
    free(obj);
}
