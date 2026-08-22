// LeetCode 2043 - Simple Bank System
// https://leetcode.com/problems/simple-bank-system/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct {
    long long* bal;
    int n;
} Bank;

Bank* bankCreate(long long* balance, int balanceSize) {
    Bank* obj = (Bank*)malloc(sizeof(Bank));
    obj->n = balanceSize;
    obj->bal = (long long*)malloc((size_t)balanceSize * sizeof(long long));
    memcpy(obj->bal, balance, (size_t)balanceSize * sizeof(long long));
    return obj;
}

static bool bankValid(Bank* obj, int account) {
    return account >= 1 && account <= obj->n;
}

bool bankTransfer(Bank* obj, int account1, int account2, long long money) {
    if (!bankValid(obj, account1) || !bankValid(obj, account2) || obj->bal[account1 - 1] < money) return false;
    obj->bal[account1 - 1] -= money;
    obj->bal[account2 - 1] += money;
    return true;
}

bool bankDeposit(Bank* obj, int account, long long money) {
    if (!bankValid(obj, account)) return false;
    obj->bal[account - 1] += money;
    return true;
}

bool bankWithdraw(Bank* obj, int account, long long money) {
    if (!bankValid(obj, account) || obj->bal[account - 1] < money) return false;
    obj->bal[account - 1] -= money;
    return true;
}

void bankFree(Bank* obj) {
    if (!obj) return;
    free(obj->bal);
    free(obj);
}
