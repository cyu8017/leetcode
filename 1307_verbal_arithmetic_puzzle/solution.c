// LeetCode 1307 - Verbal Arithmetic Puzzle
// https://leetcode.com/problems/verbal-arithmetic-puzzle/

#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

static int value_map[128];
static bool used_digit[10];
static bool leading[128];
static char** g_words;
static int g_wordsSize;
static char* g_result;
static int g_width;

static bool solve_col(int column, int row, int total) {
    if (column == g_width) return total == 0;
    if (row < g_wordsSize) {
        int wlen = (int)strlen(g_words[row]);
        if (column >= wlen) return solve_col(column, row + 1, total);
        char ch = g_words[row][wlen - 1 - column];
        if (value_map[(unsigned char)ch] >= 0)
            return solve_col(column, row + 1, total + value_map[(unsigned char)ch]);
        for (int digit = 0; digit < 10; digit++) {
            if (!used_digit[digit] && (digit || !leading[(unsigned char)ch])) {
                value_map[(unsigned char)ch] = digit;
                used_digit[digit] = true;
                if (solve_col(column, row + 1, total + digit)) return true;
                used_digit[digit] = false;
                value_map[(unsigned char)ch] = -1;
            }
        }
        return false;
    }
    char ch = g_result[g_width - 1 - column];
    int digit = total % 10;
    int carry = total / 10;
    if (value_map[(unsigned char)ch] >= 0)
        return value_map[(unsigned char)ch] == digit && solve_col(column + 1, 0, carry);
    if (used_digit[digit] || (digit == 0 && leading[(unsigned char)ch])) return false;
    value_map[(unsigned char)ch] = digit;
    used_digit[digit] = true;
    bool ok = solve_col(column + 1, 0, carry);
    used_digit[digit] = false;
    value_map[(unsigned char)ch] = -1;
    return ok;
}

bool isSolvable(char** words, int wordsSize, char* result) {
    int maxw = 0;
    for (int i = 0; i < wordsSize; i++) {
        int L = (int)strlen(words[i]);
        if (L > maxw) maxw = L;
    }
    int rlen = (int)strlen(result);
    if (maxw > rlen) return false;
    memset(value_map, -1, sizeof(value_map));
    memset(used_digit, 0, sizeof(used_digit));
    memset(leading, 0, sizeof(leading));
    char seen[128] = {0};
    int uniq = 0;
    for (int i = 0; i < wordsSize; i++) {
        int L = (int)strlen(words[i]);
        if (L > 1) leading[(unsigned char)words[i][0]] = true;
        for (int j = 0; words[i][j]; j++) {
            unsigned char c = words[i][j];
            if (!seen[c]) { seen[c] = 1; uniq++; }
        }
    }
    if (rlen > 1) leading[(unsigned char)result[0]] = true;
    for (int j = 0; result[j]; j++) {
        unsigned char c = result[j];
        if (!seen[c]) { seen[c] = 1; uniq++; }
    }
    if (uniq > 10) return false;
    g_words = words;
    g_wordsSize = wordsSize;
    g_result = result;
    g_width = rlen;
    return solve_col(0, 0, 0);
}
