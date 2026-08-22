// LeetCode 3815 - Design Auction System
// https://leetcode.com/problems/design-auction-system/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int amount; int userID; } Bid3815;
typedef struct {
    int itemId;
    int* userIds;
    int* amounts;
    int n, cap;
    Bid3815* heap;
    int hsz, hcap;
} Item3815;

typedef struct {
    Item3815* items;
    int n, cap;
} AuctionSystem;

static Item3815* find_item(AuctionSystem* s, int itemId, bool create) {
    for (int i = 0; i < s->n; i++) if (s->items[i].itemId == itemId) return &s->items[i];
    if (!create) return NULL;
    if (s->n == s->cap) {
        s->cap = s->cap ? s->cap * 2 : 8;
        s->items = (Item3815*)realloc(s->items, (size_t)s->cap * sizeof(Item3815));
    }
    Item3815* it = &s->items[s->n++];
    it->itemId = itemId;
    it->userIds = NULL; it->amounts = NULL; it->n = 0; it->cap = 0;
    it->heap = NULL; it->hsz = 0; it->hcap = 0;
    return it;
}

static void set_bid(Item3815* it, int userId, int amount) {
    for (int i = 0; i < it->n; i++) {
        if (it->userIds[i] == userId) { it->amounts[i] = amount; goto push; }
    }
    if (it->n == it->cap) {
        it->cap = it->cap ? it->cap * 2 : 8;
        it->userIds = (int*)realloc(it->userIds, (size_t)it->cap * sizeof(int));
        it->amounts = (int*)realloc(it->amounts, (size_t)it->cap * sizeof(int));
    }
    it->userIds[it->n] = userId;
    it->amounts[it->n] = amount;
    it->n++;
push:
    if (it->hsz == it->hcap) {
        it->hcap = it->hcap ? it->hcap * 2 : 8;
        it->heap = (Bid3815*)realloc(it->heap, (size_t)it->hcap * sizeof(Bid3815));
    }
    int i = it->hsz++;
    it->heap[i] = (Bid3815){amount, userId};
    while (i > 0) {
        int p = (i - 1) / 2;
        Bid3815 a = it->heap[p], b = it->heap[i];
        if (a.amount > b.amount || (a.amount == b.amount && a.userID > b.userID)) break;
        it->heap[p] = b; it->heap[i] = a; i = p;
    }
}

static int get_amount(Item3815* it, int userId, bool* ok) {
    for (int i = 0; i < it->n; i++) if (it->userIds[i] == userId) { *ok = true; return it->amounts[i]; }
    *ok = false; return 0;
}

AuctionSystem* auctionSystemCreate(void) {
    AuctionSystem* s = (AuctionSystem*)calloc(1, sizeof(AuctionSystem));
    return s;
}

void auctionSystemAddBid(AuctionSystem* obj, int userId, int itemId, int bidAmount) {
    Item3815* it = find_item(obj, itemId, true);
    set_bid(it, userId, bidAmount);
}

void auctionSystemUpdateBid(AuctionSystem* obj, int userId, int itemId, int newAmount) {
    auctionSystemAddBid(obj, userId, itemId, newAmount);
}

void auctionSystemRemoveBid(AuctionSystem* obj, int userId, int itemId) {
    Item3815* it = find_item(obj, itemId, false);
    if (!it) return;
    for (int i = 0; i < it->n; i++) {
        if (it->userIds[i] == userId) {
            it->userIds[i] = it->userIds[it->n - 1];
            it->amounts[i] = it->amounts[it->n - 1];
            it->n--;
            return;
        }
    }
}

int auctionSystemGetHighestBidder(AuctionSystem* obj, int itemId) {
    Item3815* it = find_item(obj, itemId, false);
    if (!it) return -1;
    while (it->hsz > 0) {
        Bid3815 top = it->heap[0];
        bool ok = false;
        int amount = get_amount(it, top.userID, &ok);
        if (ok && amount == top.amount) return top.userID;
        it->heap[0] = it->heap[--it->hsz];
        int i = 0;
        for (;;) {
            int l = 2*i+1, r = 2*i+2, s = i;
            if (l < it->hsz) {
                Bid3815 a = it->heap[l], b = it->heap[s];
                if (a.amount > b.amount || (a.amount == b.amount && a.userID > b.userID)) s = l;
            }
            if (r < it->hsz) {
                Bid3815 a = it->heap[r], b = it->heap[s];
                if (a.amount > b.amount || (a.amount == b.amount && a.userID > b.userID)) s = r;
            }
            if (s == i) break;
            Bid3815 t = it->heap[i]; it->heap[i] = it->heap[s]; it->heap[s] = t;
            i = s;
        }
    }
    return -1;
}

void auctionSystemFree(AuctionSystem* obj) {
    if (!obj) return;
    for (int i = 0; i < obj->n; i++) {
        free(obj->items[i].userIds);
        free(obj->items[i].amounts);
        free(obj->items[i].heap);
    }
    free(obj->items);
    free(obj);
}
