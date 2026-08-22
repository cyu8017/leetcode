// LeetCode 1096 - Brace Expansion II
// https://leetcode.com/problems/brace-expansion-ii/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    char** items;
    int size;
    int cap;
} StrSet;

static void setInit(StrSet* s) {
    s->cap = 8;
    s->size = 0;
    s->items = (char**)malloc((size_t)s->cap * sizeof(char*));
}

static void setFree(StrSet* s) {
    for (int i = 0; i < s->size; i++) {
        free(s->items[i]);
    }
    free(s->items);
    s->items = NULL;
    s->size = 0;
}

static bool setContains(StrSet* s, const char* str) {
    for (int i = 0; i < s->size; i++) {
        if (strcmp(s->items[i], str) == 0) {
            return true;
        }
    }
    return false;
}

static void setAdd(StrSet* s, const char* str) {
    if (setContains(s, str)) {
        return;
    }
    if (s->size == s->cap) {
        s->cap *= 2;
        s->items = (char**)realloc(s->items, (size_t)s->cap * sizeof(char*));
    }
    s->items[s->size] = (char*)malloc(strlen(str) + 1);
    strcpy(s->items[s->size], str);
    s->size++;
}

static void setUnionInPlace(StrSet* a, StrSet* b) {
    for (int i = 0; i < b->size; i++) {
        setAdd(a, b->items[i]);
    }
}

static StrSet setProduct(StrSet* a, StrSet* b) {
    StrSet out;
    setInit(&out);
    for (int i = 0; i < a->size; i++) {
        for (int j = 0; j < b->size; j++) {
            size_t len = strlen(a->items[i]) + strlen(b->items[j]);
            char* merged = (char*)malloc(len + 1);
            strcpy(merged, a->items[i]);
            strcat(merged, b->items[j]);
            setAdd(&out, merged);
            free(merged);
        }
    }
    return out;
}

static int cmpStr(const void* a, const void* b) {
    return strcmp(*(const char* const*)a, *(const char* const*)b);
}

static StrSet parse(const char* expr, int* i);

static StrSet parse(const char* expr, int* i) {
    StrSet unionSet;
    setInit(&unionSet);
    StrSet cur;
    setInit(&cur);
    setAdd(&cur, "");

    while (expr[*i] && expr[*i] != '}') {
        if (expr[*i] == '{') {
            (*i)++;
            StrSet nested = parse(expr, i);
            StrSet product = setProduct(&cur, &nested);
            setFree(&cur);
            setFree(&nested);
            cur = product;
        } else if (expr[*i] == ',') {
            setUnionInPlace(&unionSet, &cur);
            setFree(&cur);
            setInit(&cur);
            setAdd(&cur, "");
            (*i)++;
        } else {
            int j = *i;
            while (expr[j] && ((expr[j] >= 'a' && expr[j] <= 'z') || (expr[j] >= 'A' && expr[j] <= 'Z'))) {
                j++;
            }
            char* token = (char*)malloc((size_t)(j - *i) + 1);
            memcpy(token, expr + *i, (size_t)(j - *i));
            token[j - *i] = '\0';
            StrSet tokenSet;
            setInit(&tokenSet);
            setAdd(&tokenSet, token);
            free(token);
            StrSet product = setProduct(&cur, &tokenSet);
            setFree(&cur);
            setFree(&tokenSet);
            cur = product;
            *i = j;
        }
    }
    setUnionInPlace(&unionSet, &cur);
    setFree(&cur);
    if (expr[*i] == '}') {
        (*i)++;
    }
    return unionSet;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** braceExpansionII(char* expression, int* returnSize) {
    int i = 0;
    StrSet result = parse(expression, &i);
    qsort(result.items, (size_t)result.size, sizeof(char*), cmpStr);
    *returnSize = result.size;
    return result.items;
}
