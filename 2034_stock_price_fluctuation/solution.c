// LeetCode 2034 - Stock Price Fluctuation
// https://leetcode.com/problems/stock-price-fluctuation/

#include <stdlib.h>

typedef struct { int price, ts; } Pair2034;
typedef struct { int key, val; int used; } MapE2034;

typedef struct {
    int latestTs;
    MapE2034* priceAt;
    int mapCap;
    Pair2034* minH;
    int minN, minCap;
    Pair2034* maxH;
    int maxN, maxCap;
} StockPrice;

static unsigned h2034(int k) { return (unsigned)k * 2654435761u; }

static void mapEnsure(StockPrice* obj) {
    int used = 0;
    for (int i = 0; i < obj->mapCap; i++) if (obj->priceAt[i].used) used++;
    if (used * 2 < obj->mapCap) return;
    int oldCap = obj->mapCap;
    MapE2034* old = obj->priceAt;
    obj->mapCap *= 2;
    obj->priceAt = (MapE2034*)calloc((size_t)obj->mapCap, sizeof(MapE2034));
    for (int i = 0; i < oldCap; i++) if (old[i].used) {
        int idx = (int)(h2034(old[i].key) & (unsigned)(obj->mapCap - 1));
        while (obj->priceAt[idx].used) idx = (idx + 1) & (obj->mapCap - 1);
        obj->priceAt[idx] = old[i];
    }
    free(old);
}

static int* mapRef(StockPrice* obj, int key, int create) {
    int idx = (int)(h2034(key) & (unsigned)(obj->mapCap - 1));
    for (;;) {
        if (!obj->priceAt[idx].used) {
            if (!create) return NULL;
            obj->priceAt[idx].used = 1;
            obj->priceAt[idx].key = key;
            obj->priceAt[idx].val = 0;
            return &obj->priceAt[idx].val;
        }
        if (obj->priceAt[idx].key == key) return &obj->priceAt[idx].val;
        idx = (idx + 1) & (obj->mapCap - 1);
    }
}

static int mapGet(StockPrice* obj, int key) {
    int* p = mapRef(obj, key, 0);
    return p ? *p : 0;
}

static void minPush(StockPrice* o, Pair2034 p) {
    if (o->minN == o->minCap) {
        o->minCap *= 2;
        o->minH = (Pair2034*)realloc(o->minH, (size_t)o->minCap * sizeof(Pair2034));
    }
    int i = o->minN++;
    o->minH[i] = p;
    while (i > 0) {
        int par = (i - 1) / 2;
        if (o->minH[par].price <= o->minH[i].price) break;
        Pair2034 t = o->minH[par]; o->minH[par] = o->minH[i]; o->minH[i] = t;
        i = par;
    }
}

static Pair2034 minPop(StockPrice* o) {
    Pair2034 top = o->minH[0];
    o->minH[0] = o->minH[--o->minN];
    int i = 0;
    for (;;) {
        int l = 2 * i + 1, r = l + 1, sm = i;
        if (l < o->minN && o->minH[l].price < o->minH[sm].price) sm = l;
        if (r < o->minN && o->minH[r].price < o->minH[sm].price) sm = r;
        if (sm == i) break;
        Pair2034 t = o->minH[i]; o->minH[i] = o->minH[sm]; o->minH[sm] = t;
        i = sm;
    }
    return top;
}

static void maxPush(StockPrice* o, Pair2034 p) {
    if (o->maxN == o->maxCap) {
        o->maxCap *= 2;
        o->maxH = (Pair2034*)realloc(o->maxH, (size_t)o->maxCap * sizeof(Pair2034));
    }
    int i = o->maxN++;
    o->maxH[i] = p;
    while (i > 0) {
        int par = (i - 1) / 2;
        if (o->maxH[par].price >= o->maxH[i].price) break;
        Pair2034 t = o->maxH[par]; o->maxH[par] = o->maxH[i]; o->maxH[i] = t;
        i = par;
    }
}

static Pair2034 maxPop(StockPrice* o) {
    Pair2034 top = o->maxH[0];
    o->maxH[0] = o->maxH[--o->maxN];
    int i = 0;
    for (;;) {
        int l = 2 * i + 1, r = l + 1, sm = i;
        if (l < o->maxN && o->maxH[l].price > o->maxH[sm].price) sm = l;
        if (r < o->maxN && o->maxH[r].price > o->maxH[sm].price) sm = r;
        if (sm == i) break;
        Pair2034 t = o->maxH[i]; o->maxH[i] = o->maxH[sm]; o->maxH[sm] = t;
        i = sm;
    }
    return top;
}

StockPrice* stockPriceCreate(void) {
    StockPrice* obj = (StockPrice*)calloc(1, sizeof(StockPrice));
    obj->mapCap = 1024;
    obj->priceAt = (MapE2034*)calloc((size_t)obj->mapCap, sizeof(MapE2034));
    obj->minCap = obj->maxCap = 16;
    obj->minH = (Pair2034*)malloc((size_t)obj->minCap * sizeof(Pair2034));
    obj->maxH = (Pair2034*)malloc((size_t)obj->maxCap * sizeof(Pair2034));
    return obj;
}

void stockPriceUpdate(StockPrice* obj, int timestamp, int price) {
    mapEnsure(obj);
    *mapRef(obj, timestamp, 1) = price;
    if (timestamp >= obj->latestTs) obj->latestTs = timestamp;
    minPush(obj, (Pair2034){price, timestamp});
    maxPush(obj, (Pair2034){price, timestamp});
}

int stockPriceCurrent(StockPrice* obj) {
    return mapGet(obj, obj->latestTs);
}

int stockPriceMaximum(StockPrice* obj) {
    for (;;) {
        Pair2034 top = obj->maxH[0];
        if (mapGet(obj, top.ts) == top.price) return top.price;
        maxPop(obj);
    }
}

int stockPriceMinimum(StockPrice* obj) {
    for (;;) {
        Pair2034 top = obj->minH[0];
        if (mapGet(obj, top.ts) == top.price) return top.price;
        minPop(obj);
    }
}

void stockPriceFree(StockPrice* obj) {
    if (!obj) return;
    free(obj->priceAt); free(obj->minH); free(obj->maxH); free(obj);
}
