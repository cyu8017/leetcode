// LeetCode 0385 - Mini Parser
// https://leetcode.com/problems/mini-parser/

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

struct NestedInteger {
    bool isInteger;
    int integer;
    struct NestedInteger** list;
    int listSize;
};

static struct NestedInteger* nestedIntegerCreate(void) {
    struct NestedInteger* item = (struct NestedInteger*)calloc(1, sizeof(struct NestedInteger));
    item->isInteger = false;
    item->list = NULL;
    item->listSize = 0;
    return item;
}

static struct NestedInteger* nestedIntegerCreateValue(int value) {
    struct NestedInteger* item = (struct NestedInteger*)calloc(1, sizeof(struct NestedInteger));
    item->isInteger = true;
    item->integer = value;
    return item;
}

static void nestedIntegerAppend(struct NestedInteger* parent, struct NestedInteger* child) {
    parent->listSize += 1;
    parent->list = (struct NestedInteger**)realloc(
        parent->list,
        (size_t)parent->listSize * sizeof(struct NestedInteger*)
    );
    parent->list[parent->listSize - 1] = child;
}

struct NestedInteger* deserialize(char* s) {
    if (!s || s[0] != '[') {
        return nestedIntegerCreateValue(atoi(s));
    }

    struct NestedInteger** stack = NULL;
    int stackSize = 0;
    struct NestedInteger* current = NULL;
    int index = 0;
    bool negative = false;
    int number = 0;
    bool hasNumber = false;

    while (s[index] != '\0') {
        char ch = s[index];
        if (ch == '[') {
            struct NestedInteger* item = nestedIntegerCreate();
            if (current) {
                stackSize += 1;
                stack = (struct NestedInteger**)realloc(
                    stack,
                    (size_t)stackSize * sizeof(struct NestedInteger*)
                );
                stack[stackSize - 1] = current;
            }
            current = item;
        } else if (ch == '-') {
            negative = true;
        } else if (isdigit((unsigned char)ch)) {
            number = number * 10 + (ch - '0');
            hasNumber = true;
        } else if (ch == ',' || ch == ']') {
            if (hasNumber) {
                nestedIntegerAppend(current, nestedIntegerCreateValue(negative ? -number : number));
                number = 0;
                negative = false;
                hasNumber = false;
            }
            if (ch == ']') {
                if (stackSize == 0) {
                    free(stack);
                    return current;
                }
                struct NestedInteger* parent = stack[stackSize - 1];
                stackSize -= 1;
                nestedIntegerAppend(parent, current);
                current = parent;
            }
        }
        index += 1;
    }

    free(stack);
    return current ? current : nestedIntegerCreate();
}
