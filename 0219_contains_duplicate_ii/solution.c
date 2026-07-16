// LeetCode 0219 - Contains Duplicate II
// https://leetcode.com/problems/contains-duplicate-ii/

#include <stdbool.h>
#include <stdlib.h>

typedef struct Node {
    int key;
    int value;
    struct Node* next;
} Node;

static unsigned int hashKey(int key) {
    return (unsigned int)(key + 100000) % 200003;
}

bool containsNearbyDuplicate(int* nums, int numsSize, int k) {
    Node** table = (Node**)calloc(200003, sizeof(Node*));
    for (int i = 0; i < numsSize; i++) {
        unsigned int bucket = hashKey(nums[i]);
        Node* node = table[bucket];
        while (node) {
            if (node->key == nums[i]) {
                if (i - node->value <= k) {
                    for (unsigned int j = 0; j < 200003; j++) {
                        Node* current = table[j];
                        while (current) {
                            Node* next = current->next;
                            free(current);
                            current = next;
                        }
                    }
                    free(table);
                    return true;
                }
                node->value = i;
                break;
            }
            node = node->next;
        }
        if (!node) {
            Node* newNode = (Node*)malloc(sizeof(Node));
            newNode->key = nums[i];
            newNode->value = i;
            newNode->next = table[bucket];
            table[bucket] = newNode;
        }
    }
    for (unsigned int j = 0; j < 200003; j++) {
        Node* current = table[j];
        while (current) {
            Node* next = current->next;
            free(current);
            current = next;
        }
    }
    free(table);
    return false;
}
