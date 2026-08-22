// LeetCode 3484 - Design Spreadsheet
// https://leetcode.com/problems/design-spreadsheet/

#include <ctype.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int cells[26][1001];
} Spreadsheet;

Spreadsheet* spreadsheetCreate(int rows) {
    (void)rows;
    Spreadsheet* obj = (Spreadsheet*)calloc(1, sizeof(Spreadsheet));
    return obj;
}

void spreadsheetSetCell(Spreadsheet* obj, char* cell, int value) {
    int col = cell[0] - 'A';
    int row = atoi(cell + 1);
    obj->cells[col][row] = value;
}

void spreadsheetResetCell(Spreadsheet* obj, char* cell) {
    int col = cell[0] - 'A';
    int row = atoi(cell + 1);
    obj->cells[col][row] = 0;
}

static int evalToken(Spreadsheet* obj, char* p) {
    if (isalpha((unsigned char)p[0])) {
        int col = p[0] - 'A';
        int row = atoi(p + 1);
        return obj->cells[col][row];
    }
    return atoi(p);
}

int spreadsheetGetValue(Spreadsheet* obj, char* formula) {
    char* f = formula;
    if (f[0] == '=') f++;
    char buf[64];
    strncpy(buf, f, sizeof(buf) - 1);
    buf[sizeof(buf) - 1] = '\0';
    char* plus = strchr(buf, '+');
    if (!plus) return evalToken(obj, buf);
    *plus = '\0';
    return evalToken(obj, buf) + evalToken(obj, plus + 1);
}

void spreadsheetFree(Spreadsheet* obj) {
    free(obj);
}
