// LeetCode 1265 - Print Immutable Linked List in Reverse
// https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

struct ImmutableListNode;

typedef void (*PrintValueFn)(struct ImmutableListNode*);
typedef struct ImmutableListNode* (*GetNextFn)(struct ImmutableListNode*);

struct ImmutableListNode {
    PrintValueFn printValue;
    GetNextFn getNext;
};

static void print_reverse(struct ImmutableListNode* head) {
    if (!head) return;
    print_reverse(head->getNext(head));
    head->printValue(head);
}

void printLinkedListInReverse(struct ImmutableListNode* head) {
    print_reverse(head);
}
