// LeetCode 0707 - Design Linked List
// https://leetcode.com/problems/design-linked-list/

#include <stdlib.h>

typedef struct LLNode {
    int val;
    struct LLNode* next;
} LLNode;

typedef struct {
    LLNode* dummy;
    int size;
} MyLinkedList;

MyLinkedList* myLinkedListCreate(void) {
    MyLinkedList* obj = (MyLinkedList*)malloc(sizeof(MyLinkedList));
    obj->dummy = (LLNode*)malloc(sizeof(LLNode));
    obj->dummy->val = 0;
    obj->dummy->next = NULL;
    obj->size = 0;
    return obj;
}

int myLinkedListGet(MyLinkedList* obj, int index) {
    if (index < 0 || index >= obj->size) {
        return -1;
    }
    LLNode* node = obj->dummy->next;
    for (int i = 0; i < index; i++) {
        node = node->next;
    }
    return node->val;
}

void myLinkedListAddAtIndex(MyLinkedList* obj, int index, int val) {
    if (index < 0 || index > obj->size) {
        return;
    }
    LLNode* prev = obj->dummy;
    for (int i = 0; i < index; i++) {
        prev = prev->next;
    }
    LLNode* node = (LLNode*)malloc(sizeof(LLNode));
    node->val = val;
    node->next = prev->next;
    prev->next = node;
    obj->size++;
}

void myLinkedListAddAtHead(MyLinkedList* obj, int val) {
    myLinkedListAddAtIndex(obj, 0, val);
}

void myLinkedListAddAtTail(MyLinkedList* obj, int val) {
    myLinkedListAddAtIndex(obj, obj->size, val);
}

void myLinkedListDeleteAtIndex(MyLinkedList* obj, int index) {
    if (index < 0 || index >= obj->size) {
        return;
    }
    LLNode* prev = obj->dummy;
    for (int i = 0; i < index; i++) {
        prev = prev->next;
    }
    LLNode* dead = prev->next;
    prev->next = dead->next;
    free(dead);
    obj->size--;
}

void myLinkedListFree(MyLinkedList* obj) {
    LLNode* n = obj->dummy;
    while (n) {
        LLNode* next = n->next;
        free(n);
        n = next;
    }
    free(obj);
}
