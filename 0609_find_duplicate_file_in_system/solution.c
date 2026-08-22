// LeetCode 0609 - Find Duplicate File in System
// https://leetcode.com/problems/find-duplicate-file-in-system/

#define _POSIX_C_SOURCE 200809L
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char* content;
    char** paths;
    int count;
    int capacity;
} Group;

static void groupAdd(Group* group, const char* path) {
    if (group->count == group->capacity) {
        group->capacity = group->capacity ? group->capacity * 2 : 4;
        group->paths = (char**)realloc(group->paths, (size_t)group->capacity * sizeof(char*));
    }
    group->paths[group->count++] = strdup(path);
}

char*** findDuplicate(char** paths, int pathsSize, int* returnSize, int** returnColumnSizes) {
    Group* groups = NULL;
    int groupCount = 0;
    int groupCap = 0;

    for (int p = 0; p < pathsSize; p++) {
        char* entry = strdup(paths[p]);
        char* save = NULL;
        char* directory = strtok_r(entry, " ", &save);
        char* fileInfo;
        while ((fileInfo = strtok_r(NULL, " ", &save)) != NULL) {
            char* open = strchr(fileInfo, '(');
            if (!open) {
                continue;
            }
            *open = '\0';
            char* content = open + 1;
            int clen = (int)strlen(content);
            if (clen > 0 && content[clen - 1] == ')') {
                content[clen - 1] = '\0';
            }
            char full[1024];
            snprintf(full, sizeof(full), "%s/%s", directory, fileInfo);

            int found = -1;
            for (int g = 0; g < groupCount; g++) {
                if (strcmp(groups[g].content, content) == 0) {
                    found = g;
                    break;
                }
            }
            if (found < 0) {
                if (groupCount == groupCap) {
                    groupCap = groupCap ? groupCap * 2 : 8;
                    groups = (Group*)realloc(groups, (size_t)groupCap * sizeof(Group));
                }
                groups[groupCount].content = strdup(content);
                groups[groupCount].paths = NULL;
                groups[groupCount].count = 0;
                groups[groupCount].capacity = 0;
                found = groupCount++;
            }
            groupAdd(&groups[found], full);
        }
        free(entry);
    }

    int outCount = 0;
    for (int g = 0; g < groupCount; g++) {
        if (groups[g].count > 1) {
            outCount++;
        }
    }
    char*** result = (char***)malloc((size_t)outCount * sizeof(char**));
    *returnColumnSizes = (int*)malloc((size_t)outCount * sizeof(int));
    int idx = 0;
    for (int g = 0; g < groupCount; g++) {
        if (groups[g].count > 1) {
            result[idx] = groups[g].paths;
            (*returnColumnSizes)[idx] = groups[g].count;
            idx++;
        } else {
            for (int i = 0; i < groups[g].count; i++) {
                free(groups[g].paths[i]);
            }
            free(groups[g].paths);
        }
        free(groups[g].content);
    }
    free(groups);
    *returnSize = outCount;
    return result;
}
