// LeetCode 0901 - Online Stock Span
// https://leetcode.com/problems/online-stock-span/

#include <stdlib.h>

typedef struct {
    int* prices;
    int* spans;
    int size;
    int capacity;
} StockSpanner;

StockSpanner* stockSpannerCreate(void) {
    StockSpanner* obj = (StockSpanner*)malloc(sizeof(StockSpanner));
    obj->capacity = 16;
    obj->size = 0;
    obj->prices = (int*)malloc((size_t)obj->capacity * sizeof(int));
    obj->spans = (int*)malloc((size_t)obj->capacity * sizeof(int));
    return obj;
}

int stockSpannerNext(StockSpanner* obj, int price) {
    int span = 1;
    while (obj->size > 0 && obj->prices[obj->size - 1] <= price) {
        span += obj->spans[--obj->size];
    }
    if (obj->size == obj->capacity) {
        obj->capacity *= 2;
        obj->prices = (int*)realloc(obj->prices, (size_t)obj->capacity * sizeof(int));
        obj->spans = (int*)realloc(obj->spans, (size_t)obj->capacity * sizeof(int));
    }
    obj->prices[obj->size] = price;
    obj->spans[obj->size] = span;
    obj->size++;
    return span;
}

void stockSpannerFree(StockSpanner* obj) {
    free(obj->prices);
    free(obj->spans);
    free(obj);
}
