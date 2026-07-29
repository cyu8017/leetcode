// LeetCode 0425 - Word Squares
// https://leetcode.com/problems/word-squares/

#include <stdlib.h>
#include <string.h>

typedef struct {
    char*** squares;
    int count;
    int capacity;
    int wordLen;
} SquareCollector;

static void addSquare(SquareCollector* collector, char** current) {
    if (collector->count == collector->capacity) {
        collector->capacity = collector->capacity == 0 ? 8 : collector->capacity * 2;
        collector->squares = (char***)realloc(collector->squares, (size_t)collector->capacity * sizeof(char**));
    }
    char** square = (char**)malloc((size_t)collector->wordLen * sizeof(char*));
    for (int i = 0; i < collector->wordLen; i++) {
        square[i] = current[i];
    }
    collector->squares[collector->count++] = square;
}

static void dfs(char** words, int wordsSize, int wordLen, char** current, int row, SquareCollector* collector) {
    if (row == wordLen) {
        addSquare(collector, current);
        return;
    }

    char prefix[16];
    for (int i = 0; i < row; i++) {
        prefix[i] = current[i][row];
    }
    prefix[row] = '\0';

    for (int w = 0; w < wordsSize; w++) {
        if (strncmp(words[w], prefix, (size_t)row) != 0) {
            continue;
        }
        current[row] = words[w];
        dfs(words, wordsSize, wordLen, current, row + 1, collector);
    }
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** wordSquares(char** words, int wordsSize, int* returnSize, int** returnColumnSizes) {
    if (wordsSize == 0) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    int wordLen = (int)strlen(words[0]);
    char** current = (char**)malloc((size_t)wordLen * sizeof(char*));
    SquareCollector collector = {0};
    collector.wordLen = wordLen;
    dfs(words, wordsSize, wordLen, current, 0, &collector);
    free(current);

    *returnSize = collector.count;
    *returnColumnSizes = (int*)malloc((size_t)collector.count * sizeof(int));
    for (int i = 0; i < collector.count; i++) {
        (*returnColumnSizes)[i] = wordLen;
    }
    return collector.squares;
}
