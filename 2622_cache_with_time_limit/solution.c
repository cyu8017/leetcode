// LeetCode 2622 - Cache With Time Limit
// https://leetcode.com/problems/cache-with-time-limit/

#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

typedef struct Node {
    int key;
    int value;
    long long expire;
    struct Node* next;
} Node;

typedef struct {
    Node* head;
} TimeLimitedCache;

static long long now_ms(void) {
    struct timespec ts;
    clock_gettime(CLOCK_REALTIME, &ts);
    return (long long)ts.tv_sec * 1000LL + ts.tv_nsec / 1000000LL;
}

TimeLimitedCache* timeLimitedCacheCreate(void) {
    return (TimeLimitedCache*)calloc(1, sizeof(TimeLimitedCache));
}

bool timeLimitedCacheSet(TimeLimitedCache* obj, int key, int value, int duration) {
    long long now = now_ms();
    bool alive = false;
    for (Node* n = obj->head; n; n = n->next) {
        if (n->key == key) {
            alive = n->expire > now;
            n->value = value;
            n->expire = now + duration;
            return alive;
        }
    }
    Node* node = (Node*)malloc(sizeof(Node));
    node->key = key; node->value = value; node->expire = now + duration;
    node->next = obj->head;
    obj->head = node;
    return false;
}

int timeLimitedCacheGet(TimeLimitedCache* obj, int key) {
    long long now = now_ms();
    for (Node* n = obj->head; n; n = n->next) {
        if (n->key == key) {
            if (n->expire <= now) return -1;
            return n->value;
        }
    }
    return -1;
}

int timeLimitedCacheCount(TimeLimitedCache* obj) {
    long long now = now_ms();
    int cnt = 0;
    Node** pp = &obj->head;
    while (*pp) {
        if ((*pp)->expire > now) { cnt++; pp = &(*pp)->next; }
        else {
            Node* dead = *pp;
            *pp = dead->next;
            free(dead);
        }
    }
    return cnt;
}

void timeLimitedCacheFree(TimeLimitedCache* obj) {
    Node* n = obj->head;
    while (n) { Node* nx = n->next; free(n); n = nx; }
    free(obj);
}
