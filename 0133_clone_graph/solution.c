// LeetCode 0133 - Clone Graph
#include <stdlib.h>
struct Node { int val; int numNeighbors; struct Node** neighbors; };

static struct Node **originals, **copies;
static int count;
static struct Node* clone(struct Node* node) {
    if (!node) return NULL;
    for (int i = 0; i < count; ++i) if (originals[i] == node) return copies[i];
    struct Node *copy = malloc(sizeof(struct Node));
    copy->val = node->val;
    copy->numNeighbors = node->numNeighbors;
    copy->neighbors = malloc(copy->numNeighbors * sizeof(struct Node *));
    originals[count] = node; copies[count++] = copy;
    for (int i = 0; i < node->numNeighbors; ++i) copy->neighbors[i] = clone(node->neighbors[i]);
    return copy;
}
struct Node* cloneGraph(struct Node* node) {
    if (!node) return NULL;
    originals = malloc(101 * sizeof(struct Node *));
    copies = malloc(101 * sizeof(struct Node *));
    count = 0;
    struct Node *answer = clone(node);
    free(originals); free(copies);
    return answer;
}