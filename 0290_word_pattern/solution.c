// LeetCode 0290 - Word Pattern
// https://leetcode.com/problems/word-pattern/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct Mapping {
    char key;
    char* value;
    struct Mapping* next;
} Mapping;

typedef struct WordMapping {
    char* word;
    char value;
    struct WordMapping* next;
} WordMapping;

static bool mappingContains(Mapping* head, char key, const char* value) {
    for (Mapping* current = head; current != NULL; current = current->next) {
        if (current->key == key) {
            return strcmp(current->value, value) == 0;
        }
    }
    return false;
}

static bool mappingHasKey(Mapping* head, char key) {
    for (Mapping* current = head; current != NULL; current = current->next) {
        if (current->key == key) {
            return true;
        }
    }
    return false;
}

static void mappingAdd(Mapping** head, char key, const char* value) {
    Mapping* node = (Mapping*)malloc(sizeof(Mapping));
    node->key = key;
    node->value = strdup(value);
    node->next = *head;
    *head = node;
}

static bool wordMappingHasKey(WordMapping* head, const char* word) {
    for (WordMapping* current = head; current != NULL; current = current->next) {
        if (strcmp(current->word, word) == 0) {
            return true;
        }
    }
    return false;
}

static void wordMappingAdd(WordMapping** head, const char* word, char value) {
    WordMapping* node = (WordMapping*)malloc(sizeof(WordMapping));
    node->word = strdup(word);
    node->value = value;
    node->next = *head;
    *head = node;
}

static int splitWords(const char* s, char*** words) {
    int count = 0;
    int capacity = 0;
    *words = NULL;
    const char* start = s;

    while (*s != '\0') {
        while (*s == ' ') {
            s++;
        }
        if (*s == '\0') {
            break;
        }
        start = s;
        while (*s != '\0' && *s != ' ') {
            s++;
        }
        if (count == capacity) {
            capacity = capacity == 0 ? 4 : capacity * 2;
            *words = (char**)realloc(*words, (size_t)capacity * sizeof(char*));
        }
        int length = (int)(s - start);
        char* word = (char*)malloc((size_t)length + 1);
        memcpy(word, start, (size_t)length);
        word[length] = '\0';
        (*words)[count++] = word;
    }
    return count;
}

bool wordPattern(char* pattern, char* s) {
    char** words = NULL;
    int wordCount = splitWords(s, &words);
    int patternLength = (int)strlen(pattern);
    if (patternLength != wordCount) {
        for (int index = 0; index < wordCount; index++) {
            free(words[index]);
        }
        free(words);
        return false;
    }

    Mapping* charToWord = NULL;
    WordMapping* wordToChar = NULL;
    bool result = true;

    for (int index = 0; index < patternLength; index++) {
        char ch = pattern[index];
        const char* word = words[index];
        if (mappingHasKey(charToWord, ch)) {
            if (!mappingContains(charToWord, ch, word)) {
                result = false;
                break;
            }
        } else {
            if (wordMappingHasKey(wordToChar, word)) {
                result = false;
                break;
            }
            mappingAdd(&charToWord, ch, word);
            wordMappingAdd(&wordToChar, word, ch);
        }
    }

    for (Mapping* current = charToWord; current != NULL;) {
        Mapping* next = current->next;
        free(current->value);
        free(current);
        current = next;
    }
    for (WordMapping* current = wordToChar; current != NULL;) {
        WordMapping* next = current->next;
        free(current->word);
        free(current);
        current = next;
    }
    for (int index = 0; index < wordCount; index++) {
        free(words[index]);
    }
    free(words);
    return result;
}
