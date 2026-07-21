// LeetCode 1801 - Number of Orders in the Backlog
// https://leetcode.com/problems/number-of-orders-in-the-backlog/

#include <stdlib.h>

typedef struct {
    int price;
    int amount;
} Order;

typedef struct {
    Order* data;
    int size;
    int capacity;
} OrderHeap;

static void heapEnsure(OrderHeap* h) {
    if (h->size < h->capacity) return;
    h->capacity = h->capacity ? h->capacity * 2 : 8;
    h->data = (Order*)realloc(h->data, (size_t)h->capacity * sizeof(Order));
}

static void buyPush(OrderHeap* h, int price, int amount) {
    heapEnsure(h);
    int i = h->size++;
    h->data[i].price = price;
    h->data[i].amount = amount;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->data[p].price >= h->data[i].price) break;
        Order t = h->data[p];
        h->data[p] = h->data[i];
        h->data[i] = t;
        i = p;
    }
}

static Order buyPop(OrderHeap* h) {
    Order top = h->data[0];
    h->data[0] = h->data[--h->size];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = l + 1, best = i;
        if (l < h->size && h->data[l].price > h->data[best].price) best = l;
        if (r < h->size && h->data[r].price > h->data[best].price) best = r;
        if (best == i) break;
        Order t = h->data[i];
        h->data[i] = h->data[best];
        h->data[best] = t;
        i = best;
    }
    return top;
}

static void sellPush(OrderHeap* h, int price, int amount) {
    heapEnsure(h);
    int i = h->size++;
    h->data[i].price = price;
    h->data[i].amount = amount;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->data[p].price <= h->data[i].price) break;
        Order t = h->data[p];
        h->data[p] = h->data[i];
        h->data[i] = t;
        i = p;
    }
}

static Order sellPop(OrderHeap* h) {
    Order top = h->data[0];
    h->data[0] = h->data[--h->size];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = l + 1, best = i;
        if (l < h->size && h->data[l].price < h->data[best].price) best = l;
        if (r < h->size && h->data[r].price < h->data[best].price) best = r;
        if (best == i) break;
        Order t = h->data[i];
        h->data[i] = h->data[best];
        h->data[best] = t;
        i = best;
    }
    return top;
}

int getNumberOfBacklogOrders(int** orders, int ordersSize, int* ordersColSize) {
    (void)ordersColSize;
    OrderHeap buy = {0}, sell = {0};
    const int MOD = 1000000007;
    for (int i = 0; i < ordersSize; i++) {
        int price = orders[i][0], amount = orders[i][1], type = orders[i][2];
        if (type == 0) buyPush(&buy, price, amount);
        else sellPush(&sell, price, amount);
        while (buy.size && sell.size && buy.data[0].price >= sell.data[0].price) {
            Order b = buyPop(&buy);
            Order s = sellPop(&sell);
            int matched = b.amount < s.amount ? b.amount : s.amount;
            b.amount -= matched;
            s.amount -= matched;
            if (b.amount) buyPush(&buy, b.price, b.amount);
            if (s.amount) sellPush(&sell, s.price, s.amount);
        }
    }
    long long total = 0;
    for (int i = 0; i < buy.size; i++) total = (total + buy.data[i].amount) % MOD;
    for (int i = 0; i < sell.size; i++) total = (total + sell.data[i].amount) % MOD;
    free(buy.data);
    free(sell.data);
    return (int)total;
}
