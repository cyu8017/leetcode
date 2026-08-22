// LeetCode 0411 - Minimum Unique Word Abbreviation
// https://leetcode.com/problems/minimum-unique-word-abbreviation/

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static bool matches(const char* word, const char* abbr) {
    int index = 0;
    int pointer = 0;
    int wordLen = (int)strlen(word);
    int abbrLen = (int)strlen(abbr);

    while (index < wordLen && pointer < abbrLen) {
        if (isdigit((unsigned char)abbr[pointer])) {
            if (abbr[pointer] == '0') {
                return false;
            }
            int number = 0;
            while (pointer < abbrLen && isdigit((unsigned char)abbr[pointer])) {
                number = number * 10 + (abbr[pointer] - '0');
                pointer++;
            }
            index += number;
        } else {
            if (index >= wordLen || word[index] != abbr[pointer]) {
                return false;
            }
            index++;
            pointer++;
        }
    }

    return index == wordLen && pointer == abbrLen;
}

typedef struct {
    char** items;
    int size;
    int capacity;
} WordList;

static void word_list_init(WordList* list) {
    list->items = NULL;
    list->size = 0;
    list->capacity = 0;
}

static void word_list_add(WordList* list, const char* word) {
    if (list->size == list->capacity) {
        list->capacity = list->capacity ? list->capacity * 2 : 8;
        list->items = (char**)realloc(list->items, (size_t)list->capacity * sizeof(char*));
    }
    list->items[list->size++] = strdup(word);
}

static void word_list_free(WordList* list) {
    for (int index = 0; index < list->size; index++) {
        free(list->items[index]);
    }
    free(list->items);
    list->items = NULL;
    list->size = 0;
    list->capacity = 0;
}

typedef struct {
    char** parts;
    int count;
    int capacity;
} PartList;

static void part_list_init(PartList* list) {
    list->parts = NULL;
    list->count = 0;
    list->capacity = 0;
}

static void part_list_copy(PartList* dest, const PartList* src) {
    part_list_init(dest);
    for (int index = 0; index < src->count; index++) {
        if (dest->count == dest->capacity) {
            dest->capacity = dest->capacity ? dest->capacity * 2 : 8;
            dest->parts = (char**)realloc(dest->parts, (size_t)dest->capacity * sizeof(char*));
        }
        dest->parts[dest->count++] = strdup(src->parts[index]);
    }
}

static void part_list_add(PartList* list, const char* part) {
    if (list->count == list->capacity) {
        list->capacity = list->capacity ? list->capacity * 2 : 8;
        list->parts = (char**)realloc(list->parts, (size_t)list->capacity * sizeof(char*));
    }
    list->parts[list->count++] = strdup(part);
}

static void part_list_free(PartList* list) {
    for (int index = 0; index < list->count; index++) {
        free(list->parts[index]);
    }
    free(list->parts);
    list->parts = NULL;
    list->count = 0;
    list->capacity = 0;
}

static char* build_abbr(const PartList* parts, int skip) {
    size_t length = 0;
    for (int index = 0; index < parts->count; index++) {
        length += strlen(parts->parts[index]);
    }
    char skipBuffer[16] = "";
    if (skip) {
        snprintf(skipBuffer, sizeof(skipBuffer), "%d", skip);
        length += strlen(skipBuffer);
    }

    char* abbr = (char*)malloc(length + 1);
    abbr[0] = '\0';
    for (int index = 0; index < parts->count; index++) {
        strcat(abbr, parts->parts[index]);
    }
    if (skip) {
        strcat(abbr, skipBuffer);
    }
    return abbr;
}

static bool valid_abbr(
    const char* target,
    const WordList* words,
    const char* abbr
) {
    if (!matches(target, abbr)) {
        return false;
    }
    for (int index = 0; index < words->size; index++) {
        if (matches(words->items[index], abbr)) {
            return false;
        }
    }
    return true;
}

static void dfs(
    const char* target,
    const WordList* words,
    int index,
    PartList* parts,
    int skip,
    int* bestLen,
    char** result
) {
    int targetLen = (int)strlen(target);
    if (index == targetLen) {
        char* abbr = build_abbr(parts, skip);
        if (valid_abbr(target, words, abbr)) {
            int abbrLen = (int)strlen(abbr);
            if (abbrLen < *bestLen || (abbrLen == *bestLen && strcmp(abbr, *result) < 0)) {
                *bestLen = abbrLen;
                free(*result);
                *result = abbr;
                return;
            }
        }
        free(abbr);
        return;
    }

    dfs(target, words, index + 1, parts, skip + 1, bestLen, result);

    PartList newParts;
    part_list_copy(&newParts, parts);
    if (skip) {
        char skipBuffer[16];
        snprintf(skipBuffer, sizeof(skipBuffer), "%d", skip);
        part_list_add(&newParts, skipBuffer);
    }
    char letter[2] = {target[index], '\0'};
    part_list_add(&newParts, letter);
    dfs(target, words, index + 1, &newParts, 0, bestLen, result);
    part_list_free(&newParts);
}

char* minAbbreviation(char* target, char** dictionary, int dictionarySize) {
    WordList words;
    word_list_init(&words);
    int targetLen = (int)strlen(target);
    for (int index = 0; index < dictionarySize; index++) {
        if ((int)strlen(dictionary[index]) == targetLen) {
            word_list_add(&words, dictionary[index]);
        }
    }

    int bestLen = targetLen + 1;
    char* result = strdup(target);
    PartList parts;
    part_list_init(&parts);
    dfs(target, &words, 0, &parts, 0, &bestLen, &result);
    part_list_free(&parts);
    word_list_free(&words);
    return result;
}
