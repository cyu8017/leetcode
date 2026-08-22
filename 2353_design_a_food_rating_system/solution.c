// LeetCode 2353 - Design a Food Rating System
// https://leetcode.com/problems/design-a-food-rating-system/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct { char* food; int rating; } Item;
typedef struct { Item* data; int size; int cap; } FoodHeap;

typedef struct {
    char** foods;
    char** cuisines;
    int* ratings;
    int n;
    FoodHeap* heaps; /* parallel to unique cuisines - use simple linear maps */
    char** cuisineKeys;
    int cuisineCount;
    int cuisineCap;
} FoodRatings;

static int cmpItem(Item a, Item b) {
    if (a.rating != b.rating) return b.rating - a.rating; /* higher first */
    return strcmp(a.food, b.food);
}

static void heapPush(FoodHeap* h, Item it) {
    if (h->size >= h->cap) {
        h->cap = h->cap ? h->cap * 2 : 8;
        h->data = (Item*)realloc(h->data, (size_t)h->cap * sizeof(Item));
    }
    int i = h->size++;
    h->data[i] = it;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (cmpItem(h->data[p], h->data[i]) <= 0) break;
        Item t = h->data[p]; h->data[p] = h->data[i]; h->data[i] = t;
        i = p;
    }
}

static void heapPop(FoodHeap* h) {
    h->data[0] = h->data[--h->size];
    int i = 0;
    while (1) {
        int l = 2*i+1, r = 2*i+2, best = i;
        if (l < h->size && cmpItem(h->data[l], h->data[best]) < 0) best = l;
        if (r < h->size && cmpItem(h->data[r], h->data[best]) < 0) best = r;
        if (best == i) break;
        Item t = h->data[i]; h->data[i] = h->data[best]; h->data[best] = t;
        i = best;
    }
}

static int findCuisine(FoodRatings* obj, const char* c) {
    for (int i = 0; i < obj->cuisineCount; i++)
        if (strcmp(obj->cuisineKeys[i], c) == 0) return i;
    return -1;
}

static int findFood(FoodRatings* obj, const char* food) {
    for (int i = 0; i < obj->n; i++)
        if (strcmp(obj->foods[i], food) == 0) return i;
    return -1;
}

FoodRatings* foodRatingsCreate(char** foods, int foodsSize, char** cuisines, int cuisinesSize, int* ratings, int ratingsSize) {
    (void)cuisinesSize; (void)ratingsSize;
    FoodRatings* obj = (FoodRatings*)calloc(1, sizeof(FoodRatings));
    obj->n = foodsSize;
    obj->foods = (char**)malloc((size_t)foodsSize * sizeof(char*));
    obj->cuisines = (char**)malloc((size_t)foodsSize * sizeof(char*));
    obj->ratings = (int*)malloc((size_t)foodsSize * sizeof(int));
    for (int i = 0; i < foodsSize; i++) {
        obj->foods[i] = foods[i];
        obj->cuisines[i] = cuisines[i];
        obj->ratings[i] = ratings[i];
        int ci = findCuisine(obj, cuisines[i]);
        if (ci < 0) {
            if (obj->cuisineCount >= obj->cuisineCap) {
                obj->cuisineCap = obj->cuisineCap ? obj->cuisineCap * 2 : 8;
                obj->cuisineKeys = (char**)realloc(obj->cuisineKeys, (size_t)obj->cuisineCap * sizeof(char*));
                obj->heaps = (FoodHeap*)realloc(obj->heaps, (size_t)obj->cuisineCap * sizeof(FoodHeap));
            }
            ci = obj->cuisineCount++;
            obj->cuisineKeys[ci] = cuisines[i];
            memset(&obj->heaps[ci], 0, sizeof(FoodHeap));
        }
        Item it = {foods[i], ratings[i]};
        heapPush(&obj->heaps[ci], it);
    }
    return obj;
}

void foodRatingsChangeRating(FoodRatings* obj, char* food, int newRating) {
    int fi = findFood(obj, food);
    obj->ratings[fi] = newRating;
    int ci = findCuisine(obj, obj->cuisines[fi]);
    Item it = {obj->foods[fi], newRating};
    heapPush(&obj->heaps[ci], it);
}

char* foodRatingsHighestRated(FoodRatings* obj, char* cuisine) {
    int ci = findCuisine(obj, cuisine);
    FoodHeap* h = &obj->heaps[ci];
    while (1) {
        Item top = h->data[0];
        int fi = findFood(obj, top.food);
        if (obj->ratings[fi] == top.rating) return top.food;
        heapPop(h);
    }
}

void foodRatingsFree(FoodRatings* obj) {
    if (!obj) return;
    for (int i = 0; i < obj->cuisineCount; i++) free(obj->heaps[i].data);
    free(obj->heaps);
    free(obj->cuisineKeys);
    free(obj->foods);
    free(obj->cuisines);
    free(obj->ratings);
    free(obj);
}
