// LeetCode 2166 - Design Bitset
// https://leetcode.com/problems/design-bitset/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct {
    char* bits;
    int ones;
    bool flipped;
    int size;
} Bitset;

Bitset* bitsetCreate(int size) {
    Bitset* obj = (Bitset*)malloc(sizeof(Bitset));
    obj->bits = (char*)calloc((size_t)size, 1);
    obj->ones = 0;
    obj->flipped = false;
    obj->size = size;
    return obj;
}

void bitsetFix(Bitset* obj, int idx) {
    char target = obj->flipped ? 0 : 1;
    if (obj->bits[idx] != target) {
        obj->bits[idx] = target;
        if (obj->flipped) obj->ones--;
        else obj->ones++;
    }
}

void bitsetUnfix(Bitset* obj, int idx) {
    char target = obj->flipped ? 1 : 0;
    if (obj->bits[idx] != target) {
        obj->bits[idx] = target;
        if (obj->flipped) obj->ones++;
        else obj->ones--;
    }
}

void bitsetFlip(Bitset* obj) {
    obj->flipped = !obj->flipped;
    obj->ones = obj->size - obj->ones;
}

bool bitsetAll(Bitset* obj) { return obj->ones == obj->size; }
bool bitsetOne(Bitset* obj) { return obj->ones > 0; }
int bitsetCount(Bitset* obj) { return obj->ones; }

char* bitsetToString(Bitset* obj) {
    char* b = (char*)malloc((size_t)obj->size + 1);
    for (int i = 0; i < obj->size; i++) {
        char v = obj->bits[i];
        if (obj->flipped) v ^= 1;
        b[i] = (char)('0' + v);
    }
    b[obj->size] = '\0';
    return b;
}

void bitsetFree(Bitset* obj) {
    if (!obj) return;
    free(obj->bits);
    free(obj);
}
