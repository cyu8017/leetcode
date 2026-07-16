// LeetCode 0380 - Insert Delete GetRandom O(1)
// https://leetcode.com/problems/insert-delete-getrandom-o1/

#include <stdbool.h>
#include <stdlib.h>
typedef struct {
    int key;
    int value;
    bool used;
} HashEntry;

typedef struct {
    int* values;
    int count;
    int capacity;
    HashEntry* entries;
    int entryCapacity;
} RandomizedSet;

static unsigned int hashKey(int key) {
    return (unsigned int)key * 2654435761u;
}

static int findEntry(RandomizedSet* obj, int key, bool create) {
    unsigned int hash = hashKey(key);
    int index = (int)(hash & (unsigned int)(obj->entryCapacity - 1));

    for (;;) {
        if (!obj->entries[index].used) {
            if (create) {
                obj->entries[index].used = true;
                obj->entries[index].key = key;
                return index;
            }
            return -1;
        }
        if (obj->entries[index].key == key) {
            return index;
        }
        index = (index + 1) & (obj->entryCapacity - 1);
    }
}

static void resizeEntries(RandomizedSet* obj) {
    int oldCapacity = obj->entryCapacity;
    HashEntry* oldEntries = obj->entries;
    obj->entryCapacity *= 2;
    obj->entries = (HashEntry*)calloc((size_t)obj->entryCapacity, sizeof(HashEntry));

    for (int index = 0; index < oldCapacity; index++) {
        if (oldEntries[index].used) {
            int slot = findEntry(obj, oldEntries[index].key, true);
            obj->entries[slot].value = oldEntries[index].value;
        }
    }

    free(oldEntries);
}

RandomizedSet* randomizedSetCreate() {
    RandomizedSet* obj = (RandomizedSet*)calloc(1, sizeof(RandomizedSet));
    obj->capacity = 4;
    obj->values = (int*)malloc((size_t)obj->capacity * sizeof(int));
    obj->entryCapacity = 16;
    obj->entries = (HashEntry*)calloc((size_t)obj->entryCapacity, sizeof(HashEntry));
    return obj;
}

bool randomizedSetInsert(RandomizedSet* obj, int val) {
    if (obj->count * 2 >= obj->entryCapacity && obj->entryCapacity > 0) {
        resizeEntries(obj);
    }

    int slot = findEntry(obj, val, false);
    if (slot >= 0) {
        return false;
    }

    slot = findEntry(obj, val, true);
    if (obj->count >= obj->capacity) {
        obj->capacity *= 2;
        obj->values = (int*)realloc(obj->values, (size_t)obj->capacity * sizeof(int));
    }

    obj->entries[slot].value = obj->count;
    obj->values[obj->count] = val;
    obj->count += 1;
    return true;
}

bool randomizedSetRemove(RandomizedSet* obj, int val) {
    int slot = findEntry(obj, val, false);
    if (slot < 0) {
        return false;
    }

    int index = obj->entries[slot].value;
    int lastValue = obj->values[obj->count - 1];
    obj->values[index] = lastValue;
    obj->entries[findEntry(obj, lastValue, false)].value = index;
    obj->count -= 1;
    obj->entries[slot].used = false;
    return true;
}

int randomizedSetGetRandom(RandomizedSet* obj) {
    return obj->values[rand() % obj->count];
}

void randomizedSetFree(RandomizedSet* obj) {
    free(obj->values);
    free(obj->entries);
    free(obj);
}
