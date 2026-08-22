// LeetCode 0726 - Number of Atoms
// https://leetcode.com/problems/number-of-atoms/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>

typedef struct {
    char atom[12];
    int count;
} AtomCount;

typedef struct {
    AtomCount* items;
    int size;
    int capacity;
} Counter;

static void counterInit(Counter* c) {
    c->items = NULL;
    c->size = 0;
    c->capacity = 0;
}

static void counterAdd(Counter* c, const char* atom, int count) {
    for (int i = 0; i < c->size; i++) {
        if (strcmp(c->items[i].atom, atom) == 0) {
            c->items[i].count += count;
            return;
        }
    }
    if (c->size == c->capacity) {
        c->capacity = c->capacity ? c->capacity * 2 : 8;
        c->items = (AtomCount*)realloc(c->items, (size_t)c->capacity * sizeof(AtomCount));
    }
    strncpy(c->items[c->size].atom, atom, sizeof(c->items[c->size].atom) - 1);
    c->items[c->size].atom[sizeof(c->items[c->size].atom) - 1] = '\0';
    c->items[c->size].count = count;
    c->size++;
}

static void counterMerge(Counter* dst, Counter* src, int mult) {
    for (int i = 0; i < src->size; i++) {
        counterAdd(dst, src->items[i].atom, src->items[i].count * mult);
    }
}

static int cmpAtom(const void* a, const void* b) {
    return strcmp(((const AtomCount*)a)->atom, ((const AtomCount*)b)->atom);
}

char* countOfAtoms(char* formula) {
    Counter stack[100];
    int top = 0;
    counterInit(&stack[top++]);
    int i = 0;
    int n = (int)strlen(formula);

    while (i < n) {
        if (formula[i] == '(') {
            counterInit(&stack[top++]);
            i++;
        } else if (formula[i] == ')') {
            i++;
            int start = i;
            while (i < n && isdigit((unsigned char)formula[i])) {
                i++;
            }
            int mult = start == i ? 1 : atoi(formula + start);
            Counter topC = stack[--top];
            counterMerge(&stack[top - 1], &topC, mult);
            free(topC.items);
        } else {
            int start = i++;
            while (i < n && islower((unsigned char)formula[i])) {
                i++;
            }
            char atom[12];
            int alen = i - start;
            if (alen > 11) alen = 11;
            memcpy(atom, formula + start, (size_t)alen);
            atom[alen] = '\0';
            start = i;
            while (i < n && isdigit((unsigned char)formula[i])) {
                i++;
            }
            int count = start == i ? 1 : atoi(formula + start);
            counterAdd(&stack[top - 1], atom, count);
        }
    }

    Counter counts = stack[0];
    qsort(counts.items, (size_t)counts.size, sizeof(AtomCount), cmpAtom);
    char* out = (char*)malloc(10000);
    out[0] = '\0';
    for (int k = 0; k < counts.size; k++) {
        strcat(out, counts.items[k].atom);
        if (counts.items[k].count > 1) {
            char num[16];
            sprintf(num, "%d", counts.items[k].count);
            strcat(out, num);
        }
    }
    free(counts.items);
    return out;
}
