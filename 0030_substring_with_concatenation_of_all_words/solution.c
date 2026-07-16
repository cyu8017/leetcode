// LeetCode 0030 - Substring with Concatenation of All Words
// https://leetcode.com/problems/substring-with-concatenation-of-all-words/

#include <stdlib.h>
#include <string.h>

typedef struct {
    char* word;
    int need;
    int current;
} WordFreq;

static int cmp_int(const void* a, const void* b) {
    return (*(const int*)a) - (*(const int*)b);
}

static int find_word_index(WordFreq* freqs, int freqSize, int wordLen, const char* s, int pos) {
    for (int i = 0; i < freqSize; i++) {
        if (strncmp(freqs[i].word, s + pos, (size_t)wordLen) == 0) {
            return i;
        }
    }
    return -1;
}

static int find_word_in_list(char** words, int wordsSize, const char* word) {
    for (int i = 0; i < wordsSize; i++) {
        if (strcmp(words[i], word) == 0) {
            return i;
        }
    }
    return -1;
}

int* findSubstring(char* s, char** words, int wordsSize, int* returnSize) {
    *returnSize = 0;
    if (wordsSize == 0 || s == NULL || s[0] == '\0') {
        return NULL;
    }

    int wordLen = (int)strlen(words[0]);
    int wordCount = wordsSize;
    WordFreq* freqs = (WordFreq*)calloc((size_t)wordsSize, sizeof(WordFreq));
    int freqSize = 0;

    for (int i = 0; i < wordsSize; i++) {
        int idx = find_word_in_list(words, freqSize, words[i]);
        if (idx == -1) {
            freqs[freqSize].word = words[i];
            freqs[freqSize].need = 1;
            freqs[freqSize].current = 0;
            freqSize++;
        } else {
            freqs[idx].need++;
        }
    }

    int sLen = (int)strlen(s);
    int capacity = 16;
    int* result = (int*)malloc((size_t)capacity * sizeof(int));

    for (int start = 0; start < wordLen; start++) {
        for (int i = 0; i < freqSize; i++) {
            freqs[i].current = 0;
        }

        int left = start;
        int used = 0;

        for (int right = start; right <= sLen - wordLen; right += wordLen) {
            int idx = find_word_index(freqs, freqSize, wordLen, s, right);
            if (idx == -1) {
                for (int i = 0; i < freqSize; i++) {
                    freqs[i].current = 0;
                }
                used = 0;
                left = right + wordLen;
                continue;
            }

            freqs[idx].current++;
            used++;
            while (freqs[idx].current > freqs[idx].need) {
                int leftIdx = find_word_index(freqs, freqSize, wordLen, s, left);
                freqs[leftIdx].current--;
                used--;
                left += wordLen;
            }

            if (used == wordCount) {
                if (*returnSize >= capacity) {
                    capacity *= 2;
                    result = (int*)realloc(result, (size_t)capacity * sizeof(int));
                }
                result[*returnSize] = left;
                (*returnSize)++;
            }
        }
    }

    free(freqs);
    qsort(result, (size_t)(*returnSize), sizeof(int), cmp_int);
    result = (int*)realloc(result, (size_t)(*returnSize) * sizeof(int));
    return result;
}
