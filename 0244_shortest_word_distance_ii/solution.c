// LeetCode 0244 - Shortest Word Distance II
// https://leetcode.com/problems/shortest-word-distance-ii/

#include <limits.h>
#include <stdlib.h>
#include <string.h>

typedef struct WordEntry {
    char* word;
    int* indices;
    int size;
    int capacity;
    struct WordEntry* next;
} WordEntry;

typedef struct {
    WordEntry* head;
} WordDistance;

static WordEntry* find_entry(WordEntry* head, const char* word) {
    for (WordEntry* current = head; current != NULL; current = current->next) {
        if (strcmp(current->word, word) == 0) {
            return current;
        }
    }
    return NULL;
}

static void add_index(WordEntry* entry, int index) {
    if (entry->size == entry->capacity) {
        entry->capacity = entry->capacity == 0 ? 4 : entry->capacity * 2;
        entry->indices = (int*)realloc(entry->indices, entry->capacity * sizeof(int));
    }
    entry->indices[entry->size++] = index;
}

WordDistance* wordDistanceCreate(char** wordsDict, int wordsDictSize) {
    WordDistance* obj = (WordDistance*)malloc(sizeof(WordDistance));
    obj->head = NULL;
    for (int index = 0; index < wordsDictSize; ++index) {
        WordEntry* entry = find_entry(obj->head, wordsDict[index]);
        if (entry == NULL) {
            entry = (WordEntry*)malloc(sizeof(WordEntry));
            entry->word = wordsDict[index];
            entry->indices = NULL;
            entry->size = 0;
            entry->capacity = 0;
            entry->next = obj->head;
            obj->head = entry;
        }
        add_index(entry, index);
    }
    return obj;
}

int wordDistanceShortest(WordDistance* obj, char* word1, char* word2) {
    WordEntry* left = find_entry(obj->head, word1);
    WordEntry* right = find_entry(obj->head, word2);
    int i = 0;
    int j = 0;
    int best = INT_MAX;
    while (i < left->size && j < right->size) {
        int distance = left->indices[i] - right->indices[j];
        if (distance < 0) {
            distance = -distance;
        }
        if (distance < best) {
            best = distance;
        }
        if (left->indices[i] <= right->indices[j]) {
            i++;
        } else {
            j++;
        }
    }
    return best;
}

void wordDistanceFree(WordDistance* obj) {
    WordEntry* current = obj->head;
    while (current != NULL) {
        WordEntry* next = current->next;
        free(current->indices);
        free(current);
        current = next;
    }
    free(obj);
}
