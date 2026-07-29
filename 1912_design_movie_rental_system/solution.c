// LeetCode 1912 - Design Movie Rental System
// https://leetcode.com/problems/design-movie-rental-system/

#include <stdlib.h>
#include <string.h>

typedef struct { int price; int shop; } Avail;
typedef struct { int price; int shop; int movie; } Rent;
typedef struct { int shop; int movie; int price; } PriceKey;

typedef struct {
    PriceKey* prices;
    int priceN;
    Avail** available;
    int* availSize;
    int* availCap;
    int maxMovie;
    Rent* rented;
    int rentedSize;
    int rentedCap;
} MovieRentingSystem;

static int priceCmp(const void* a, const void* b) {
    const PriceKey* x = a; const PriceKey* y = b;
    if (x->shop != y->shop) return x->shop - y->shop;
    return x->movie - y->movie;
}

static int getPrice(MovieRentingSystem* obj, int shop, int movie) {
    PriceKey key = {shop, movie, 0};
    PriceKey* found = bsearch(&key, obj->prices, (size_t)obj->priceN, sizeof(PriceKey), priceCmp);
    return found ? found->price : 0;
}

static void availInsert(Avail** arr, int* sz, int* cap, Avail v) {
    if (*sz >= *cap) {
        *cap = *cap ? *cap * 2 : 8;
        *arr = (Avail*)realloc(*arr, (size_t)(*cap) * sizeof(Avail));
    }
    int i = *sz;
    while (i > 0) {
        Avail p = (*arr)[i - 1];
        if (p.price < v.price || (p.price == v.price && p.shop < v.shop)) break;
        (*arr)[i] = p;
        i--;
    }
    (*arr)[i] = v;
    (*sz)++;
}

static void availRemove(Avail* arr, int* sz, int shop, int price) {
    for (int i = 0; i < *sz; i++) {
        if (arr[i].shop == shop && arr[i].price == price) {
            for (int j = i; j + 1 < *sz; j++) arr[j] = arr[j + 1];
            (*sz)--;
            return;
        }
    }
}

static void rentInsert(Rent** arr, int* sz, int* cap, Rent v) {
    if (*sz >= *cap) {
        *cap = *cap ? *cap * 2 : 8;
        *arr = (Rent*)realloc(*arr, (size_t)(*cap) * sizeof(Rent));
    }
    int i = *sz;
    while (i > 0) {
        Rent p = (*arr)[i - 1];
        if (p.price < v.price || (p.price == v.price && p.shop < v.shop) ||
            (p.price == v.price && p.shop == v.shop && p.movie < v.movie)) break;
        (*arr)[i] = p;
        i--;
    }
    (*arr)[i] = v;
    (*sz)++;
}

static void rentRemove(Rent* arr, int* sz, int shop, int movie, int price) {
    for (int i = 0; i < *sz; i++) {
        if (arr[i].shop == shop && arr[i].movie == movie && arr[i].price == price) {
            for (int j = i; j + 1 < *sz; j++) arr[j] = arr[j + 1];
            (*sz)--;
            return;
        }
    }
}

MovieRentingSystem* movieRentingSystemCreate(int n, int** entries, int entriesSize, int* entriesColSize) {
    (void)n; (void)entriesColSize;
    MovieRentingSystem* obj = (MovieRentingSystem*)calloc(1, sizeof(MovieRentingSystem));
    obj->prices = (PriceKey*)malloc((size_t)entriesSize * sizeof(PriceKey));
    obj->priceN = entriesSize;
    int maxMovie = 0;
    for (int i = 0; i < entriesSize; i++) {
        obj->prices[i].shop = entries[i][0];
        obj->prices[i].movie = entries[i][1];
        obj->prices[i].price = entries[i][2];
        if (entries[i][1] > maxMovie) maxMovie = entries[i][1];
    }
    qsort(obj->prices, (size_t)entriesSize, sizeof(PriceKey), priceCmp);
    obj->maxMovie = maxMovie;
    obj->available = (Avail**)calloc((size_t)maxMovie + 1, sizeof(Avail*));
    obj->availSize = (int*)calloc((size_t)maxMovie + 1, sizeof(int));
    obj->availCap = (int*)calloc((size_t)maxMovie + 1, sizeof(int));
    for (int i = 0; i < entriesSize; i++) {
        int shop = entries[i][0], movie = entries[i][1], price = entries[i][2];
        availInsert(&obj->available[movie], &obj->availSize[movie], &obj->availCap[movie], (Avail){price, shop});
    }
    return obj;
}

int* movieRentingSystemSearch(MovieRentingSystem* obj, int movie, int* returnSize) {
    int* res = (int*)malloc(5 * sizeof(int));
    int sz = 0;
    if (movie <= obj->maxMovie) {
        int lim = obj->availSize[movie] < 5 ? obj->availSize[movie] : 5;
        for (int i = 0; i < lim; i++) res[sz++] = obj->available[movie][i].shop;
    }
    *returnSize = sz;
    return res;
}

void movieRentingSystemRent(MovieRentingSystem* obj, int shop, int movie) {
    int price = getPrice(obj, shop, movie);
    availRemove(obj->available[movie], &obj->availSize[movie], shop, price);
    rentInsert(&obj->rented, &obj->rentedSize, &obj->rentedCap, (Rent){price, shop, movie});
}

void movieRentingSystemDrop(MovieRentingSystem* obj, int shop, int movie) {
    int price = getPrice(obj, shop, movie);
    rentRemove(obj->rented, &obj->rentedSize, shop, movie, price);
    availInsert(&obj->available[movie], &obj->availSize[movie], &obj->availCap[movie], (Avail){price, shop});
}

int** movieRentingSystemReport(MovieRentingSystem* obj, int* returnSize, int** returnColumnSizes) {
    int lim = obj->rentedSize < 5 ? obj->rentedSize : 5;
    int** res = (int**)malloc((size_t)lim * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)lim * sizeof(int));
    for (int i = 0; i < lim; i++) {
        res[i] = (int*)malloc(2 * sizeof(int));
        res[i][0] = obj->rented[i].shop;
        res[i][1] = obj->rented[i].movie;
        (*returnColumnSizes)[i] = 2;
    }
    *returnSize = lim;
    return res;
}

void movieRentingSystemFree(MovieRentingSystem* obj) {
    if (!obj) return;
    free(obj->prices);
    for (int i = 0; i <= obj->maxMovie; i++) free(obj->available[i]);
    free(obj->available);
    free(obj->availSize);
    free(obj->availCap);
    free(obj->rented);
    free(obj);
}
