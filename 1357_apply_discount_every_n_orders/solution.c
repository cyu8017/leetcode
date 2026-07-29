// LeetCode 1357 - Apply Discount Every n Orders
// https://leetcode.com/problems/apply-discount-every-n-orders/

#include <stdlib.h>

typedef struct {
    int n;
    int discount;
    int* price; // indexed by product id up to 200
    int count;
} Cashier;

Cashier* cashierCreate(int n, int discount, int* products, int productsSize, int* prices, int pricesSize) {
    (void)pricesSize;
    Cashier* obj = (Cashier*)calloc(1, sizeof(Cashier));
    obj->n = n;
    obj->discount = discount;
    obj->price = (int*)calloc(201, sizeof(int));
    for (int i = 0; i < productsSize; i++) obj->price[products[i]] = prices[i];
    return obj;
}

double cashierGetBill(Cashier* obj, int* product, int productSize, int* amount, int amountSize) {
    (void)amountSize;
    obj->count++;
    double total = 0;
    for (int i = 0; i < productSize; i++) total += (double)obj->price[product[i]] * amount[i];
    if (obj->count % obj->n == 0) total = total * (100 - obj->discount) / 100.0;
    return total;
}

void cashierFree(Cashier* obj) {
    free(obj->price);
    free(obj);
}
