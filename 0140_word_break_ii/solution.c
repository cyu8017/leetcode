// LeetCode 0140 - Word Break II
#include <stdlib.h>
#include <string.h>
static char **answers, *sentence, **dictionary;
static int count, capacity, n, dictionarySize;
static void add(char *text) {
    if (count == capacity) { capacity *= 2; answers = realloc(answers, capacity * sizeof(char *)); }
    answers[count++] = text;
}
static void dfs(char *s, int start, int length) {
    if (start == n) {
        sentence[length] = '\0';
        char *copy = malloc(length + 1); memcpy(copy, sentence, length + 1); add(copy);
        return;
    }
    for (int w = 0; w < dictionarySize; ++w) {
        int wordLength = strlen(dictionary[w]);
        if (start + wordLength > n || strncmp(s + start, dictionary[w], wordLength)) continue;
        int position = length;
        if (length) sentence[length++] = ' ';
        memcpy(sentence + length, dictionary[w], wordLength);
        dfs(s, start + wordLength, length + wordLength);
        length = position;
    }
}
char** wordBreak(char* s, char** wordDict, int wordDictSize, int* returnSize) {
    n = strlen(s); dictionary = wordDict; dictionarySize = wordDictSize; count = 0; capacity = 16;
    answers = malloc(capacity * sizeof(char *)); sentence = malloc(2 * n + 1);
    dfs(s, 0, 0);
    free(sentence); *returnSize = count; return answers;
}