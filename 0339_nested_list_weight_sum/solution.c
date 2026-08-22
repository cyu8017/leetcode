// LeetCode 0339 - Nested List Weight Sum
// https://leetcode.com/problems/nested-list-weight-sum/

struct NestedInteger {
    int isInteger;
    int integer;
    struct NestedInteger* children;
    int childrenSize;
};

static void dfs(struct NestedInteger* items, int itemsSize, int depth, int* total) {
    for (int index = 0; index < itemsSize; index++) {
        struct NestedInteger* item = &items[index];
        if (item->isInteger) {
            *total += item->integer * depth;
        } else {
            dfs(item->children, item->childrenSize, depth + 1, total);
        }
    }
}

int depthSum(struct NestedInteger* nestedList, int nestedListSize) {
    int total = 0;
    dfs(nestedList, nestedListSize, 1, &total);
    return total;
}
