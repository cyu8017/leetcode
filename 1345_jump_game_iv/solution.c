// LeetCode 1345 - Jump Game IV
// https://leetcode.com/problems/jump-game-iv/

#include <stdlib.h>
#include <stdbool.h>

typedef struct Node { int idx; struct Node* next; } Node;

int minJumps(int* arr, int arrSize) {
    if (arrSize <= 1) return 0;
    // hash map value -> list of indices (open addressing bucket by value% size)
    int buckets = arrSize * 2 + 7;
    Node** map = (Node**)calloc(buckets, sizeof(Node*));
    bool* used_key = (bool*)calloc(buckets, sizeof(bool));
    for (int i = 0; i < arrSize; i++) {
        unsigned h = ((unsigned)arr[i] * 2654435761u) % buckets;
        Node* node = (Node*)malloc(sizeof(Node));
        node->idx = i;
        node->next = map[h];
        map[h] = node;
    }
    bool* seen = (bool*)calloc(arrSize, sizeof(bool));
    int* queue = (int*)malloc(arrSize * sizeof(int));
    int qh = 0, qt = 0;
    queue[qt++] = 0;
    seen[0] = true;
    int steps = 0;
    while (qh < qt) {
        int sz = qt - qh;
        for (int s = 0; s < sz; s++) {
            int i = queue[qh++];
            if (i == arrSize - 1) {
                for (int b = 0; b < buckets; b++) {
                    Node* cur = map[b];
                    while (cur) { Node* n = cur->next; free(cur); cur = n; }
                }
                free(map); free(used_key); free(seen); free(queue);
                return steps;
            }
            unsigned h = ((unsigned)arr[i] * 2654435761u) % buckets;
            // collect same-value neighbors then clear that chain carefully
            // scan all buckets for matching value (collision-safe)
            for (int b = 0; b < buckets; b++) {
                Node** link = &map[b];
                while (*link) {
                    if (arr[(*link)->idx] == arr[i]) {
                        int j = (*link)->idx;
                        if (!seen[j]) { seen[j] = true; queue[qt++] = j; }
                        Node* dead = *link;
                        *link = dead->next;
                        free(dead);
                    } else link = &(*link)->next;
                }
            }
            for (int j = i - 1; j <= i + 1; j += 2) {
                if (j >= 0 && j < arrSize && !seen[j]) {
                    seen[j] = true;
                    queue[qt++] = j;
                }
            }
        }
        steps++;
    }
    free(map); free(used_key); free(seen); free(queue);
    return -1;
}
