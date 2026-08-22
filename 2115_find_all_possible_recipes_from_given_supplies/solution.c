// LeetCode 2115 - Find All Possible Recipes from Given Supplies
// https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct { char* key; int val; int used; } HInt;
typedef struct { char* key; int* list; int len; int cap; int used; } HList;

static unsigned hashStr(const char* s) {
    unsigned h = 2166136261u;
    for (; *s; s++) { h ^= (unsigned char)*s; h *= 16777619u; }
    return h;
}

static int hintGet(HInt* t, int cap, const char* k, int* found) {
    unsigned h = hashStr(k) % (unsigned)cap;
    for (int i = 0; i < cap; i++) {
        unsigned idx = (h + i) % (unsigned)cap;
        if (!t[idx].used) { *found = 0; return (int)idx; }
        if (strcmp(t[idx].key, k) == 0) { *found = 1; return (int)idx; }
    }
    *found = 0; return -1;
}

char** findAllRecipes(char** recipes, int recipesSize, char*** ingredients, int ingredientsSize, int* ingredientsColSize, char** supplies, int suppliesSize, int* returnSize) {
    (void)ingredientsSize;
    int cap = 4096;
    HInt* indeg = calloc((size_t)cap, sizeof(HInt));
    HList* graph = calloc((size_t)cap, sizeof(HList));
    for (int i = 0; i < recipesSize; i++) {
        int f; int idx = hintGet(indeg, cap, recipes[i], &f);
        indeg[idx].key = recipes[i]; indeg[idx].val = ingredientsColSize[i]; indeg[idx].used = 1;
        for (int j = 0; j < ingredientsColSize[i]; j++) {
            char* ing = ingredients[i][j];
            unsigned h = hashStr(ing) % (unsigned)cap;
            int gidx = -1;
            for (int k = 0; k < cap; k++) {
                unsigned ii = (h + k) % (unsigned)cap;
                if (!graph[ii].used) { gidx = (int)ii; graph[ii].key = ing; graph[ii].used = 1; break; }
                if (strcmp(graph[ii].key, ing) == 0) { gidx = (int)ii; break; }
            }
            HList* g = &graph[gidx];
            if (g->len == g->cap) {
                g->cap = g->cap ? g->cap * 2 : 4;
                g->list = realloc(g->list, (size_t)g->cap * sizeof(int));
            }
            g->list[g->len++] = i;
        }
    }
    char** q = malloc((size_t)(recipesSize + suppliesSize + 5) * sizeof(char*));
    int qh = 0, qt = 0;
    for (int i = 0; i < suppliesSize; i++) q[qt++] = supplies[i];
    char** ans = malloc((size_t)recipesSize * sizeof(char*));
    int an = 0;
    bool* done = calloc((size_t)recipesSize, sizeof(bool));
    while (qh < qt) {
        char* cur = q[qh++];
        unsigned h = hashStr(cur) % (unsigned)cap;
        for (int k = 0; k < cap; k++) {
            unsigned ii = (h + k) % (unsigned)cap;
            if (!graph[ii].used) break;
            if (strcmp(graph[ii].key, cur) != 0) continue;
            for (int t = 0; t < graph[ii].len; t++) {
                int ri = graph[ii].list[t];
                int f; int idx = hintGet(indeg, cap, recipes[ri], &f);
                if (--indeg[idx].val == 0 && !done[ri]) {
                    done[ri] = true;
                    ans[an++] = recipes[ri];
                    q[qt++] = recipes[ri];
                }
            }
            break;
        }
    }
    for (int i = 0; i < cap; i++) free(graph[i].list);
    free(indeg); free(graph); free(q); free(done);
    *returnSize = an;
    return ans;
}
