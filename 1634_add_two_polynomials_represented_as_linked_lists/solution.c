// LeetCode 1634 - Add Two Polynomials Represented as Linked Lists
// https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/

#include <stdlib.h>

struct PolyNode {
    int coefficient;
    int power;
    struct PolyNode* next;
};

struct PolyNode* addPoly(struct PolyNode* poly1, struct PolyNode* poly2) {
    struct PolyNode dummy = {0, 0, NULL};
    struct PolyNode* cur = &dummy;
    while (poly1 || poly2) {
        int c, p;
        if (!poly2 || (poly1 && poly1->power > poly2->power)) {
            c = poly1->coefficient; p = poly1->power; poly1 = poly1->next;
        } else if (!poly1 || poly2->power > poly1->power) {
            c = poly2->coefficient; p = poly2->power; poly2 = poly2->next;
        } else {
            c = poly1->coefficient + poly2->coefficient;
            p = poly1->power;
            poly1 = poly1->next;
            poly2 = poly2->next;
        }
        if (c) {
            cur->next = (struct PolyNode*)malloc(sizeof(struct PolyNode));
            cur->next->coefficient = c;
            cur->next->power = p;
            cur->next->next = NULL;
            cur = cur->next;
        }
    }
    return dummy.next;
}
