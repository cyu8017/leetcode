// LeetCode 3822 - Design Order Management System
// https://leetcode.com/problems/design-order-management-system/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    int orderId;
    char* orderType;
    int price;
    bool used;
} Order3822;

typedef struct {
    Order3822* orders;
    int n, cap;
} OrderManagementSystem;

OrderManagementSystem* orderManagementSystemCreate(void) {
    return (OrderManagementSystem*)calloc(1, sizeof(OrderManagementSystem));
}

void orderManagementSystemAddOrder(OrderManagementSystem* obj, int orderId, char* orderType, int price) {
    if (obj->n == obj->cap) {
        obj->cap = obj->cap ? obj->cap * 2 : 8;
        obj->orders = (Order3822*)realloc(obj->orders, (size_t)obj->cap * sizeof(Order3822));
    }
    Order3822* o = &obj->orders[obj->n++];
    o->orderId = orderId;
    o->orderType = strdup(orderType);
    o->price = price;
    o->used = true;
}

void orderManagementSystemModifyOrder(OrderManagementSystem* obj, int orderId, int newPrice) {
    for (int i = 0; i < obj->n; i++) {
        if (obj->orders[i].used && obj->orders[i].orderId == orderId) {
            obj->orders[i].price = newPrice;
            return;
        }
    }
}

void orderManagementSystemCancelOrder(OrderManagementSystem* obj, int orderId) {
    for (int i = 0; i < obj->n; i++) {
        if (obj->orders[i].used && obj->orders[i].orderId == orderId) {
            obj->orders[i].used = false;
            free(obj->orders[i].orderType);
            obj->orders[i].orderType = NULL;
            return;
        }
    }
}

int* orderManagementSystemGetOrdersAtPrice(OrderManagementSystem* obj, char* orderType, int price, int* returnSize) {
    int* ans = (int*)malloc((size_t)(obj->n + 1) * sizeof(int));
    int asz = 0;
    for (int i = 0; i < obj->n; i++) {
        if (obj->orders[i].used && obj->orders[i].price == price &&
            obj->orders[i].orderType && strcmp(obj->orders[i].orderType, orderType) == 0) {
            ans[asz++] = obj->orders[i].orderId;
        }
    }
    *returnSize = asz;
    return ans;
}

void orderManagementSystemFree(OrderManagementSystem* obj) {
    if (!obj) return;
    for (int i = 0; i < obj->n; i++) free(obj->orders[i].orderType);
    free(obj->orders);
    free(obj);
}
