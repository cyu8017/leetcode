// LeetCode 1258 - Synonymous Sentences
// https://leetcode.com/problems/synonymous-sentences/

#include <stdlib.h>
#include <string.h>

typedef struct {
    char word[32];
    char parent[32];
} WordEntry;

static int cmp_str(const void* a, const void* b) {
    return strcmp(*(const char* const*)a, *(const char* const*)b);
}

static char* find_parent(WordEntry* entries, int* count, const char* word) {
    for (int i = 0; i < *count; i++) {
        if (strcmp(entries[i].word, word) == 0) {
            if (strcmp(entries[i].parent, entries[i].word) != 0) {
                char* root = find_parent(entries, count, entries[i].parent);
                strncpy(entries[i].parent, root, sizeof(entries[i].parent) - 1);
            }
            return entries[i].parent;
        }
    }
    strncpy(entries[*count].word, word, sizeof(entries[*count].word) - 1);
    strncpy(entries[*count].parent, word, sizeof(entries[*count].parent) - 1);
    (*count)++;
    return entries[*count - 1].parent;
}

static void unite(WordEntry* entries, int* count, const char* a, const char* b) {
    char* ra = find_parent(entries, count, a);
    char* rb = find_parent(entries, count, b);
    if (strcmp(ra, rb) != 0) {
        for (int i = 0; i < *count; i++) {
            if (strcmp(entries[i].word, rb) == 0) {
                strncpy(entries[i].parent, ra, sizeof(entries[i].parent) - 1);
                break;
            }
        }
    }
}

char** generateSentences(char*** synonyms, int synonymsSize, int* synonymsColSize, char* text, int* returnSize) {
    (void)synonymsColSize;
    WordEntry entries[256];
    int entryCount = 0;
    for (int i = 0; i < synonymsSize; i++) unite(entries, &entryCount, synonyms[i][0], synonyms[i][1]);
    char tokens[64][32];
    int tokenCount = 0;
    int i = 0;
    while (text[i]) {
        while (text[i] == ' ') i++;
        if (!text[i]) break;
        int j = 0;
        while (text[i] && text[i] != ' ') tokens[tokenCount][j++] = text[i++];
        tokens[tokenCount][j] = '\0';
        tokenCount++;
    }
    char choices[64][32][32];
    int choiceSizes[64];
    for (int t = 0; t < tokenCount; t++) {
        char* root = find_parent(entries, &entryCount, tokens[t]);
        choiceSizes[t] = 0;
        for (int j = 0; j < entryCount; j++) {
            if (strcmp(find_parent(entries, &entryCount, entries[j].word), root) != 0) continue;
            int dup = 0;
            for (int k = 0; k < choiceSizes[t]; k++) {
                if (strcmp(choices[t][k], entries[j].word) == 0) dup = 1;
            }
            if (!dup) strncpy(choices[t][choiceSizes[t]++], entries[j].word, 31);
        }
        for (int a = 0; a < choiceSizes[t]; a++) {
            for (int b = a + 1; b < choiceSizes[t]; b++) {
                if (strcmp(choices[t][a], choices[t][b]) > 0) {
                    char tmp[32];
                    strcpy(tmp, choices[t][a]);
                    strcpy(choices[t][a], choices[t][b]);
                    strcpy(choices[t][b], tmp);
                }
            }
        }
    }
    int cap = 128, count = 0;
    char** result = (char**)malloc((size_t)cap * sizeof(char*));
    int idx[64] = {0};
    for (;;) {
        char buf[512] = {0};
        for (int t = 0; t < tokenCount; t++) {
            if (t) strcat(buf, " ");
            strcat(buf, choices[t][idx[t]]);
        }
        if (count >= cap) {
            cap *= 2;
            result = (char**)realloc(result, (size_t)cap * sizeof(char*));
        }
        result[count++] = strdup(buf);
        int carry = tokenCount - 1;
        while (carry >= 0) {
            idx[carry]++;
            if (idx[carry] < choiceSizes[carry]) break;
            idx[carry] = 0;
            carry--;
        }
        if (carry < 0) break;
    }
    qsort(result, (size_t)count, sizeof(char*), cmp_str);
    *returnSize = count;
    return result;
}
