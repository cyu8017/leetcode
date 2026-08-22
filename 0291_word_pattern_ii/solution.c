// LeetCode 0291 - Word Pattern II
// https://leetcode.com/problems/word-pattern-ii/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct CharMapping {
    char key;
    char* value;
    struct CharMapping* next;
} CharMapping;

typedef struct WordMapping {
    char* word;
    char value;
    struct WordMapping* next;
} WordMapping;

static bool charMappingHasKey(CharMapping* head, char key) {
    for (CharMapping* current = head; current != NULL; current = current->next) {
        if (current->key == key) {
            return true;
        }
    }
    return false;
}

static char* charMappingGet(CharMapping* head, char key) {
    for (CharMapping* current = head; current != NULL; current = current->next) {
        if (current->key == key) {
            return current->value;
        }
    }
    return NULL;
}

static void charMappingAdd(CharMapping** head, char key, const char* value) {
    CharMapping* node = (CharMapping*)malloc(sizeof(CharMapping));
    node->key = key;
    node->value = strdup(value);
    node->next = *head;
    *head = node;
}

static void charMappingRemove(CharMapping** head, char key) {
    CharMapping** current = head;
    while (*current != NULL) {
        if ((*current)->key == key) {
            CharMapping* next = (*current)->next;
            free((*current)->value);
            free(*current);
            *current = next;
            return;
        }
        current = &(*current)->next;
    }
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

static void wordMappingRemove(WordMapping** head, const char* word) {
    WordMapping** current = head;
    while (*current != NULL) {
        if (strcmp((*current)->word, word) == 0) {
            WordMapping* next = (*current)->next;
            free((*current)->word);
            free(*current);
            *current = next;
            return;
        }
        current = &(*current)->next;
    }
}

static void freeCharMappings(CharMapping* head) {
    while (head != NULL) {
        CharMapping* next = head->next;
        free(head->value);
        free(head);
        head = next;
    }
}

static void freeWordMappings(WordMapping* head) {
    while (head != NULL) {
        WordMapping* next = head->next;
        free(head->word);
        free(head);
        head = next;
    }
}

static bool backtrack(
    const char* pattern,
    const char* s,
    int patternIndex,
    int stringIndex,
    CharMapping** charToWord,
    WordMapping** wordToChar
) {
    if (pattern[patternIndex] == '\0') {
        return s[stringIndex] == '\0';
    }

    char ch = pattern[patternIndex];
    if (charMappingHasKey(*charToWord, ch)) {
        const char* word = charMappingGet(*charToWord, ch);
        int wordLength = (int)strlen(word);
        if (strncmp(s + stringIndex, word, (size_t)wordLength) != 0) {
            return false;
        }
        return backtrack(pattern, s, patternIndex + 1, stringIndex + wordLength, charToWord, wordToChar);
    }

    int stringLength = (int)strlen(s);
    for (int end = stringIndex + 1; end <= stringLength; end++) {
        int wordLength = end - stringIndex;
        char* word = (char*)malloc((size_t)wordLength + 1);
        memcpy(word, s + stringIndex, (size_t)wordLength);
        word[wordLength] = '\0';

        if (wordMappingHasKey(*wordToChar, word)) {
            free(word);
            continue;
        }

        charMappingAdd(charToWord, ch, word);
        wordMappingAdd(wordToChar, word, ch);
        if (backtrack(pattern, s, patternIndex + 1, end, charToWord, wordToChar)) {
            free(word);
            return true;
        }
        charMappingRemove(charToWord, ch);
        wordMappingRemove(wordToChar, word);
        free(word);
    }
    return false;
}

bool wordPatternMatch(char* pattern, char* s) {
    CharMapping* charToWord = NULL;
    WordMapping* wordToChar = NULL;
    bool result = backtrack(pattern, s, 0, 0, &charToWord, &wordToChar);
    freeCharMappings(charToWord);
    freeWordMappings(wordToChar);
    return result;
}
