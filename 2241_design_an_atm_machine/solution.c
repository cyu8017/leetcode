// LeetCode 2241 - Design an ATM Machine
// https://leetcode.com/problems/design-an-atm-machine/

#include <stdlib.h>

typedef struct {
    long long cnt[5];
    int vals[5];
} ATM;

ATM* aTMCreate() {
    ATM* obj = (ATM*)calloc(1, sizeof(ATM));
    obj->vals[0] = 20;
    obj->vals[1] = 50;
    obj->vals[2] = 100;
    obj->vals[3] = 200;
    obj->vals[4] = 500;
    return obj;
}

void aTMDeposit(ATM* obj, int* banknotesCount, int banknotesCountSize) {
    (void)banknotesCountSize;
    for (int i = 0; i < 5; i++) obj->cnt[i] += banknotesCount[i];
}

int* aTMWithdraw(ATM* obj, int amount, int* returnSize) {
    int* take = (int*)calloc(5, sizeof(int));
    long long remain = amount;
    long long tmp[5];
    for (int i = 0; i < 5; i++) tmp[i] = obj->cnt[i];
    for (int i = 4; i >= 0; i--) {
        long long need = remain / obj->vals[i];
        if (need > tmp[i]) need = tmp[i];
        take[i] = (int)need;
        remain -= need * obj->vals[i];
    }
    if (remain != 0) {
        free(take);
        int* fail = (int*)malloc(sizeof(int));
        fail[0] = -1;
        *returnSize = 1;
        return fail;
    }
    for (int i = 0; i < 5; i++) obj->cnt[i] -= take[i];
    *returnSize = 5;
    return take;
}

void aTMFree(ATM* obj) {
    free(obj);
}
