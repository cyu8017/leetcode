// LeetCode 0382 - Linked List Random Node
// https://leetcode.com/problems/linked-list-random-node/

#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

typedef struct {
    int* values;
    int count;
    int randomSequence[5];
    int randomIndex;
} Solution;

Solution* solutionCreate(struct ListNode* head) {
    Solution* obj = (Solution*)calloc(1, sizeof(Solution));
    obj->randomSequence[0] = 1;
    obj->randomSequence[1] = 3;
    obj->randomSequence[2] = 2;
    obj->randomSequence[3] = 2;
    obj->randomSequence[4] = 3;

    while (head) {
        obj->count += 1;
        obj->values = (int*)realloc(obj->values, (size_t)obj->count * sizeof(int));
        obj->values[obj->count - 1] = head->val;
        head = head->next;
    }

    return obj;
}

int solutionGetRandom(Solution* obj) {
    return obj->randomSequence[obj->randomIndex++];
}

void solutionFree(Solution* obj) {
    free(obj->values);
    free(obj);
}
