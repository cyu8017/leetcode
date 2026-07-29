// LeetCode 0642 - Design Search Autocomplete System
// https://leetcode.com/problems/design-search-autocomplete-system/

#define _POSIX_C_SOURCE 200809L
#include <stdlib.h>
#include <string.h>

typedef struct {
    char** sentences;
    int* times;
    int size;
    int capacity;
    char current[200];
} AutocompleteSystem;

AutocompleteSystem* autocompleteSystemCreate(char** sentences, int sentencesSize, int* times, int timesSize) {
    (void)timesSize;
    AutocompleteSystem* obj = (AutocompleteSystem*)malloc(sizeof(AutocompleteSystem));
    obj->capacity = sentencesSize + 64;
    obj->sentences = (char**)malloc((size_t)obj->capacity * sizeof(char*));
    obj->times = (int*)malloc((size_t)obj->capacity * sizeof(int));
    obj->size = sentencesSize;
    obj->current[0] = '\0';
    for (int i = 0; i < sentencesSize; i++) {
        obj->sentences[i] = strdup(sentences[i]);
        obj->times[i] = times[i];
    }
    return obj;
}

typedef struct { char* s; int t; } Item;
static int cmpItem(const void* a, const void* b) {
    const Item* x = (const Item*)a; const Item* y = (const Item*)b;
    if (x->t != y->t) return y->t - x->t;
    return strcmp(x->s, y->s);
}

char** autocompleteSystemInput(AutocompleteSystem* obj, char c, int* retSize) {
    if (c == '#') {
        int found = -1;
        for (int i = 0; i < obj->size; i++) if (strcmp(obj->sentences[i], obj->current) == 0) { found = i; break; }
        if (found >= 0) obj->times[found]++;
        else {
            if (obj->size == obj->capacity) {
                obj->capacity *= 2;
                obj->sentences = (char**)realloc(obj->sentences, (size_t)obj->capacity * sizeof(char*));
                obj->times = (int*)realloc(obj->times, (size_t)obj->capacity * sizeof(int));
            }
            obj->sentences[obj->size] = strdup(obj->current);
            obj->times[obj->size] = 1;
            obj->size++;
        }
        obj->current[0] = '\0';
        *retSize = 0;
        return NULL;
    }
    int len = (int)strlen(obj->current);
    obj->current[len] = c; obj->current[len + 1] = '\0';
    Item* matches = (Item*)malloc((size_t)obj->size * sizeof(Item));
    int m = 0;
    int plen = (int)strlen(obj->current);
    for (int i = 0; i < obj->size; i++) {
        if (strncmp(obj->sentences[i], obj->current, (size_t)plen) == 0) {
            matches[m].s = obj->sentences[i];
            matches[m].t = obj->times[i];
            m++;
        }
    }
    qsort(matches, (size_t)m, sizeof(Item), cmpItem);
    int out = m < 3 ? m : 3;
    char** result = (char**)malloc((size_t)out * sizeof(char*));
    for (int i = 0; i < out; i++) result[i] = strdup(matches[i].s);
    free(matches);
    *retSize = out;
    return result;
}

void autocompleteSystemFree(AutocompleteSystem* obj) {
    for (int i = 0; i < obj->size; i++) free(obj->sentences[i]);
    free(obj->sentences); free(obj->times); free(obj);
}
