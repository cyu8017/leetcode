// LeetCode 0359 - Logger Rate Limiter
// https://leetcode.com/problems/logger-rate-limiter/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char* message;
    int timestamp;
} MessageEntry;

typedef struct {
    MessageEntry* entries;
    int count;
    int capacity;
} Logger;

Logger* loggerCreate() {
    return (Logger*)calloc(1, sizeof(Logger));
}

static int findMessage(Logger* obj, const char* message) {
    for (int index = 0; index < obj->count; index++) {
        if (strcmp(obj->entries[index].message, message) == 0) {
            return index;
        }
    }
    return -1;
}

bool loggerShouldPrintMessage(Logger* obj, int timestamp, char* message) {
    int index = findMessage(obj, message);
    if (index >= 0 && timestamp - obj->entries[index].timestamp < 10) {
        return false;
    }

    if (index < 0) {
        if (obj->count >= obj->capacity) {
            int newCapacity = obj->capacity == 0 ? 4 : obj->capacity * 2;
            obj->entries = (MessageEntry*)realloc(obj->entries, (size_t)newCapacity * sizeof(MessageEntry));
            obj->capacity = newCapacity;
        }
        index = obj->count++;
        obj->entries[index].message = (char*)malloc(strlen(message) + 1);
        strcpy(obj->entries[index].message, message);
    }

    obj->entries[index].timestamp = timestamp;
    return true;
}

void loggerFree(Logger* obj) {
    for (int index = 0; index < obj->count; index++) {
        free(obj->entries[index].message);
    }
    free(obj->entries);
    free(obj);
}
