// LeetCode 0403 - Frog Jump
// https://leetcode.com/problems/frog-jump/

#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int* values;
    int count;
    int capacity;
} JumpSet;

static void jump_set_add(JumpSet* set, int value) {
    for (int index = 0; index < set->count; index++) {
        if (set->values[index] == value) {
            return;
        }
    }

    if (set->count == set->capacity) {
        set->capacity = set->capacity ? set->capacity * 2 : 4;
        set->values = (int*)realloc(set->values, (size_t)set->capacity * sizeof(int));
    }

    set->values[set->count++] = value;
}

static int stone_index(int* stones, int stonesSize, int position) {
    int low = 0;
    int high = stonesSize - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (stones[mid] == position) {
            return mid;
        }
        if (stones[mid] < position) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return -1;
}

bool canCross(int* stones, int stonesSize) {
    JumpSet* jumpSets = (JumpSet*)calloc((size_t)stonesSize, sizeof(JumpSet));
    jump_set_add(&jumpSets[0], 0);

    for (int index = 0; index < stonesSize; index++) {
        for (int jumpIndex = 0; jumpIndex < jumpSets[index].count; jumpIndex++) {
            int jump = jumpSets[index].values[jumpIndex];
            for (int nextJump = jump - 1; nextJump <= jump + 1; nextJump++) {
                if (nextJump <= 0) {
                    continue;
                }

                int nextStone = stones[index] + nextJump;
                int nextIndex = stone_index(stones, stonesSize, nextStone);
                if (nextIndex >= 0) {
                    jump_set_add(&jumpSets[nextIndex], nextJump);
                }
            }
        }
    }

    bool result = jumpSets[stonesSize - 1].count > 0;

    for (int index = 0; index < stonesSize; index++) {
        free(jumpSets[index].values);
    }
    free(jumpSets);

    return result;
}
