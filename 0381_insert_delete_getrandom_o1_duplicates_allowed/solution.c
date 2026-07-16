// LeetCode 0381 - Insert Delete GetRandom O(1) - Duplicates allowed
// https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int* indices;
    int count;
    int capacity;
} IndexSet;

typedef struct {
    int key;
    IndexSet set;
    bool used;
} CollectionEntry;

typedef struct {
    int* values;
    int count;
    int capacity;
    CollectionEntry* entries;
    int entryCapacity;
} RandomizedCollection;

static unsigned int hashKey(int key) {
    return (unsigned int)key * 2654435761u;
}

static int findEntry(RandomizedCollection* obj, int key, bool create) {
    unsigned int hash = hashKey(key);
    int index = (int)(hash & (unsigned int)(obj->entryCapacity - 1));

    for (;;) {
        if (!obj->entries[index].used) {
            if (create) {
                obj->entries[index].used = true;
                obj->entries[index].key = key;
                obj->entries[index].set.indices = NULL;
                obj->entries[index].set.count = 0;
                obj->entries[index].set.capacity = 0;
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

static void resizeEntries(RandomizedCollection* obj) {
    int oldCapacity = obj->entryCapacity;
    CollectionEntry* oldEntries = obj->entries;
    obj->entryCapacity *= 2;
    obj->entries = (CollectionEntry*)calloc((size_t)obj->entryCapacity, sizeof(CollectionEntry));

    for (int index = 0; index < oldCapacity; index++) {
        if (oldEntries[index].used) {
            int slot = findEntry(obj, oldEntries[index].key, true);
            obj->entries[slot].set = oldEntries[index].set;
        }
    }

    free(oldEntries);
}

static IndexSet* getIndexSet(RandomizedCollection* obj, int key, bool create) {
    if (obj->count * 2 >= obj->entryCapacity && obj->entryCapacity > 0) {
        resizeEntries(obj);
    }

    int slot = findEntry(obj, key, create);
    if (slot < 0) {
        return NULL;
    }
    return &obj->entries[slot].set;
}

static void indexSetAdd(IndexSet* set, int index) {
    if (set->count >= set->capacity) {
        set->capacity = set->capacity == 0 ? 4 : set->capacity * 2;
        set->indices = (int*)realloc(set->indices, (size_t)set->capacity * sizeof(int));
    }
    set->indices[set->count++] = index;
}

static bool indexSetRemove(IndexSet* set, int index) {
    for (int position = 0; position < set->count; position++) {
        if (set->indices[position] == index) {
            set->indices[position] = set->indices[set->count - 1];
            set->count -= 1;
            return true;
        }
    }
    return false;
}

static int indexSetAny(const IndexSet* set) {
    return set->indices[0];
}

RandomizedCollection* randomizedCollectionCreate() {
    RandomizedCollection* obj = (RandomizedCollection*)calloc(1, sizeof(RandomizedCollection));
    obj->capacity = 4;
    obj->values = (int*)malloc((size_t)obj->capacity * sizeof(int));
    obj->entryCapacity = 16;
    obj->entries = (CollectionEntry*)calloc((size_t)obj->entryCapacity, sizeof(CollectionEntry));
    return obj;
}

bool randomizedCollectionInsert(RandomizedCollection* obj, int val) {
    IndexSet* set = getIndexSet(obj, val, true);
    bool firstInsert = set->count == 0;

    if (obj->count >= obj->capacity) {
        obj->capacity *= 2;
        obj->values = (int*)realloc(obj->values, (size_t)obj->capacity * sizeof(int));
    }

    indexSetAdd(set, obj->count);
    obj->values[obj->count] = val;
    obj->count += 1;
    return firstInsert;
}

bool randomizedCollectionRemove(RandomizedCollection* obj, int val) {
    IndexSet* set = getIndexSet(obj, val, false);
    if (!set || set->count == 0) {
        return false;
    }

    int index = indexSetAny(set);
    int lastIndex = obj->count - 1;
    int lastValue = obj->values[lastIndex];
    obj->values[index] = lastValue;

    IndexSet* lastSet = getIndexSet(obj, lastValue, false);
    indexSetRemove(lastSet, lastIndex);
    indexSetAdd(lastSet, index);

    obj->count -= 1;
    indexSetRemove(set, index);
    if (set->count == 0) {
        int slot = findEntry(obj, val, false);
        if (slot >= 0) {
            free(obj->entries[slot].set.indices);
            obj->entries[slot].set.indices = NULL;
            obj->entries[slot].set.count = 0;
            obj->entries[slot].set.capacity = 0;
            obj->entries[slot].used = false;
        }
    }
    return true;
}

int randomizedCollectionGetRandom(RandomizedCollection* obj) {
    return obj->values[obj->count - 1];
}

void randomizedCollectionFree(RandomizedCollection* obj) {
    for (int index = 0; index < obj->entryCapacity; index++) {
        if (obj->entries[index].used) {
            free(obj->entries[index].set.indices);
        }
    }
    free(obj->values);
    free(obj->entries);
    free(obj);
}
