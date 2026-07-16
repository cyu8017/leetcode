// LeetCode 0249 - Group Shifted Strings
// https://leetcode.com/problems/group-shifted-strings/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char*** groups;
    char** keys;
    int* groupSizes;
    int groupCount;
    int groupCapacity;
} GroupList;

static void group_list_init(GroupList* list) {
    list->groups = NULL;
    list->keys = NULL;
    list->groupSizes = NULL;
    list->groupCount = 0;
    list->groupCapacity = 0;
}

static int find_group_index(GroupList* list, const char* key) {
    for (int i = 0; i < list->groupCount; ++i) {
        if (strcmp(list->keys[i], key) == 0) {
            return i;
        }
    }
    return -1;
}

static void group_list_add(GroupList* list, const char* key, char* value) {
    int index = find_group_index(list, key);
    if (index < 0) {
        if (list->groupCount == list->groupCapacity) {
            list->groupCapacity = list->groupCapacity == 0 ? 4 : list->groupCapacity * 2;
            list->groups = realloc(list->groups, (size_t)list->groupCapacity * sizeof(char**));
            list->keys = realloc(list->keys, (size_t)list->groupCapacity * sizeof(char*));
            list->groupSizes = realloc(list->groupSizes, (size_t)list->groupCapacity * sizeof(int));
        }
        index = list->groupCount++;
        list->groups[index] = NULL;
        list->keys[index] = strdup(key);
        list->groupSizes[index] = 0;
    }

    int size = list->groupSizes[index];
    list->groups[index] = realloc(list->groups[index], (size_t)(size + 1) * sizeof(char*));
    list->groups[index][size] = value;
    list->groupSizes[index] = size + 1;
}

static char* make_key(const char* text) {
    if (!text || text[0] == '\0') {
        return strdup("");
    }
    int base = text[0];
    size_t length = strlen(text);
    char* key = malloc(length * 3 + 1);
    key[0] = '\0';
    for (size_t i = 0; i < length; ++i) {
        char part[8];
        snprintf(part, sizeof(part), "%s%d", i == 0 ? "" : ",", (text[i] - base + 26) % 26);
        strcat(key, part);
    }
    return key;
}

char*** groupStrings(char** strings, int stringsSize, int* returnSize, int** columnSizes) {
    GroupList list;
    group_list_init(&list);

    for (int i = 0; i < stringsSize; ++i) {
        char* key = make_key(strings[i]);
        group_list_add(&list, key, strdup(strings[i]));
        free(key);
    }

    *returnSize = list.groupCount;
    char*** result = malloc((size_t)list.groupCount * sizeof(char**));
    *columnSizes = malloc((size_t)list.groupCount * sizeof(int));
    for (int i = 0; i < list.groupCount; ++i) {
        result[i] = list.groups[i];
        (*columnSizes)[i] = list.groupSizes[i];
        free(list.keys[i]);
    }
    free(list.groups);
    free(list.keys);
    free(list.groupSizes);
    return result;
}
