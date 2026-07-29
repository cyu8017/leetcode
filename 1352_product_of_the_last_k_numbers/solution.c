// LeetCode 1352 - Product of the Last K Numbers
// https://leetcode.com/problems/product-of-the-last-k-numbers/

#include <stdlib.h>

typedef struct {
    int* p;
    int size;
    int cap;
} ProductOfNumbers;

ProductOfNumbers* productOfNumbersCreate() {
    ProductOfNumbers* obj = (ProductOfNumbers*)malloc(sizeof(ProductOfNumbers));
    obj->cap = 16; obj->size = 1;
    obj->p = (int*)malloc(obj->cap * sizeof(int));
    obj->p[0] = 1;
    return obj;
}

void productOfNumbersAdd(ProductOfNumbers* obj, int num) {
    if (num == 0) {
        obj->size = 1;
        obj->p[0] = 1;
        return;
    }
    if (obj->size == obj->cap) {
        obj->cap *= 2;
        obj->p = (int*)realloc(obj->p, obj->cap * sizeof(int));
    }
    obj->p[obj->size] = obj->p[obj->size - 1] * num;
    obj->size++;
}

int productOfNumbersGetProduct(ProductOfNumbers* obj, int k) {
    if (k >= obj->size) return 0;
    return obj->p[obj->size - 1] / obj->p[obj->size - 1 - k];
}

void productOfNumbersFree(ProductOfNumbers* obj) {
    free(obj->p);
    free(obj);
}
