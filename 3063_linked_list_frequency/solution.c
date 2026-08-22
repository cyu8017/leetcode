// LeetCode 3063 - Linked List Frequency
// https://leetcode.com/problems/linked-list-frequency/

#include <stdlib.h>
#include <stdbool.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

typedef struct { int key, val; bool used; } HEnt;
static unsigned hash_u(unsigned x) { x ^= x >> 16; x *= 0x7feb352dU; x ^= x >> 15; x *= 0x846ca68bU; x ^= x >> 16; return x; }
static void hinc(HEnt* t, int cap, int key) {
    unsigned h = hash_u((unsigned)key) & (unsigned)(cap - 1);
    while (t[h].used) {
        if (t[h].key == key) { t[h].val++; return; }
        h = (h + 1) & (unsigned)(cap - 1);
    }
    t[h].used = true; t[h].key = key; t[h].val = 1;
}

struct ListNode* frequenciesOfElements(struct ListNode* head) {
    int cap = 1 << 12;
    HEnt* t = (HEnt*)calloc((size_t)cap, sizeof(HEnt));
    for (; head; head = head->next) hinc(t, cap, head->val);
    struct ListNode dummy = {0, NULL};
    for (int i = 0; i < cap; i++) if (t[i].used) {
        struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
        node->val = t[i].val;
        node->next = dummy.next;
        dummy.next = node;
    }
    free(t);
    return dummy.next;
}
