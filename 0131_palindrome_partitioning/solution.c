// LeetCode 0131 - Palindrome Partitioning
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static char ***answers, **path;
static int *columns, count, depth, n;

static char *duplicate(char *source) {
    int length = strlen(source);
    char *copy = malloc(length + 1);
    memcpy(copy, source, length + 1);
    return copy;
}
static bool palindrome(char *s, int left, int right) {
    while (left < right) if (s[left++] != s[right--]) return false;
    return true;
}
static void dfs(char *s, int start) {
    if (start == n) {
        answers[count] = malloc(depth * sizeof(char *));
        columns[count] = depth;
        for (int i = 0; i < depth; ++i) answers[count][i] = duplicate(path[i]);
        ++count;
        return;
    }
    for (int end = start; end < n; ++end) {
        if (palindrome(s, start, end)) {
            int length = end - start + 1;
            path[depth] = malloc(length + 1);
            memcpy(path[depth], s + start, length);
            path[depth++][length] = '\0';
            dfs(s, end + 1);
            free(path[--depth]);
        }
    }
}
char*** partition(char* s, int* returnSize, int** returnColumnSizes) {
    n = strlen(s); count = depth = 0;
    int capacity = 1 << (n ? n - 1 : 0);
    answers = malloc(capacity * sizeof(char **));
    columns = malloc(capacity * sizeof(int));
    path = malloc((n ? n : 1) * sizeof(char *));
    dfs(s, 0);
    free(path);
    *returnSize = count; *returnColumnSizes = columns;
    return answers;
}