// LeetCode 0937 - Reorder Data in Log Files
// https://leetcode.com/problems/reorder-data-in-log-files/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct { char* log; char* rest; char* ident; int letter; } Item;

static int cmpItem(const void* a, const void* b) {
    const Item* x = (const Item*)a;
    const Item* y = (const Item*)b;
    if (x->letter != y->letter) return y->letter - x->letter;
    if (!x->letter) return 0;
    int c = strcmp(x->rest, y->rest);
    if (c) return c;
    return strcmp(x->ident, y->ident);
}

char** reorderLogFiles(char** logs, int logsSize, int* returnSize) {
    Item* letter = (Item*)malloc((size_t)logsSize * sizeof(Item));
    char** digit = (char**)malloc((size_t)logsSize * sizeof(char*));
    int ln = 0, dn = 0;
    for (int i = 0; i < logsSize; i++) {
        char* sp = strchr(logs[i], ' ');
        if (isalpha((unsigned char)sp[1])) {
            letter[ln].log = logs[i];
            letter[ln].ident = logs[i];
            letter[ln].rest = sp + 1;
            letter[ln].letter = 1;
            ln++;
        } else digit[dn++] = logs[i];
    }
    qsort(letter, (size_t)ln, sizeof(Item), cmpItem);
    char** ans = (char**)malloc((size_t)logsSize * sizeof(char*));
    for (int i = 0; i < ln; i++) ans[i] = letter[i].log;
    for (int i = 0; i < dn; i++) ans[ln + i] = digit[i];
    free(letter); free(digit);
    *returnSize = logsSize;
    return ans;
}
