// LeetCode 0364 - Nested List Weight Sum II
// https://leetcode.com/problems/nested-list-weight-sum-ii/

#include <stdlib.h>

struct NestedInteger {
    int isInteger;
    int integer;
    struct NestedInteger* children;
    int childrenSize;
};

typedef struct {
    int value;
    int depth;
} WeightedEntry;

typedef struct {
    WeightedEntry* entries;
    int count;
    int capacity;
} WeightedCollector;

static void weightedPush(WeightedCollector* collector, int value, int depth) {
    if (collector->count >= collector->capacity) {
        collector->capacity = collector->capacity == 0 ? 8 : collector->capacity * 2;
        collector->entries = (WeightedEntry*)realloc(
            collector->entries, (size_t)collector->capacity * sizeof(WeightedEntry));
    }
    collector->entries[collector->count].value = value;
    collector->entries[collector->count].depth = depth;
    collector->count += 1;
}

static void dfs(struct NestedInteger* items, int itemsSize, int depth, WeightedCollector* collector) {
    for (int index = 0; index < itemsSize; index++) {
        struct NestedInteger* item = &items[index];
        if (item->isInteger) {
            weightedPush(collector, item->integer, depth);
        } else {
            dfs(item->children, item->childrenSize, depth + 1, collector);
        }
    }
}

int depthSum(struct NestedInteger* nestedList, int nestedListSize) {
    WeightedCollector collector = {NULL, 0, 0};
    dfs(nestedList, nestedListSize, 1, &collector);

    if (collector.count == 0) {
        return 0;
    }

    int maxDepth = 0;
    for (int index = 0; index < collector.count; index++) {
        if (collector.entries[index].depth > maxDepth) {
            maxDepth = collector.entries[index].depth;
        }
    }

    int total = 0;
    for (int index = 0; index < collector.count; index++) {
        total += collector.entries[index].value * (maxDepth - collector.entries[index].depth + 1);
    }

    free(collector.entries);
    return total;
}
