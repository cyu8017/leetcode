// LeetCode 0288 - Unique Word Abbreviation
// https://leetcode.com/problems/unique-word-abbreviation/

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct WordNode {
    char* word;
    struct WordNode* next;
} WordNode;

typedef struct GroupNode {
    char* key;
    WordNode* words;
    int count;
    struct GroupNode* next;
} GroupNode;

typedef struct {
    GroupNode* head;
} ValidWordAbbr;

static char* abbreviate(const char* word) {
    size_t length = strlen(word);
    if (length <= 2) {
        return strdup(word);
    }
    char* key = (char*)malloc(length + 16);
    snprintf(key, length + 16, "%c%zu%c", word[0], length - 2, word[length - 1]);
    return key;
}

static GroupNode* findGroup(GroupNode* head, const char* key) {
    for (GroupNode* current = head; current != NULL; current = current->next) {
        if (strcmp(current->key, key) == 0) {
            return current;
        }
    }
    return NULL;
}

static bool groupContains(WordNode* head, const char* word) {
    for (WordNode* current = head; current != NULL; current = current->next) {
        if (strcmp(current->word, word) == 0) {
            return true;
        }
    }
    return false;
}

static void addWord(GroupNode* group, char* word) {
    if (groupContains(group->words, word)) {
        return;
    }
    WordNode* node = (WordNode*)malloc(sizeof(WordNode));
    node->word = word;
    node->next = group->words;
    group->words = node;
    group->count += 1;
}

ValidWordAbbr* validWordAbbrCreate(char** dictionary, int dictionarySize) {
    ValidWordAbbr* obj = (ValidWordAbbr*)malloc(sizeof(ValidWordAbbr));
    obj->head = NULL;

    for (int index = 0; index < dictionarySize; index++) {
        char* key = abbreviate(dictionary[index]);
        GroupNode* group = findGroup(obj->head, key);
        if (group == NULL) {
            group = (GroupNode*)malloc(sizeof(GroupNode));
            group->key = key;
            group->words = NULL;
            group->count = 0;
            group->next = obj->head;
            obj->head = group;
        } else {
            free(key);
        }
        addWord(group, dictionary[index]);
    }

    return obj;
}

bool validWordAbbrIsUnique(ValidWordAbbr* obj, char* word) {
    char* key = abbreviate(word);
    GroupNode* group = findGroup(obj->head, key);
    free(key);
    if (group == NULL) {
        return true;
    }
    return group->count == 1 && groupContains(group->words, word);
}

void validWordAbbrFree(ValidWordAbbr* obj) {
    GroupNode* group = obj->head;
    while (group != NULL) {
        GroupNode* nextGroup = group->next;
        WordNode* wordNode = group->words;
        while (wordNode != NULL) {
            WordNode* nextWord = wordNode->next;
            free(wordNode);
            wordNode = nextWord;
        }
        free(group->key);
        free(group);
        group = nextGroup;
    }
    free(obj);
}
