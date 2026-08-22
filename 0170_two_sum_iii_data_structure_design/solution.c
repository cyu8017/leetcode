// LeetCode 0170 - Two Sum III - Data structure design
#include <stdbool.h>
#include <stdlib.h>
typedef struct {
    int* numbers;
    int size;
    int capacity;
} TwoSum;
TwoSum* twoSumCreate() {
    TwoSum* obj = malloc(sizeof(TwoSum));
    obj->size = 0; obj->capacity = 16; obj->numbers = malloc(obj->capacity * sizeof(int));
    return obj;
}
void twoSumAdd(TwoSum* obj, int number) {
    if (obj->size == obj->capacity) {
        obj->capacity *= 2; obj->numbers = realloc(obj->numbers, obj->capacity * sizeof(int));
    }
    obj->numbers[obj->size++] = number;
}
bool twoSumFind(TwoSum* obj, int value) {
    for (int i = 0; i < obj->size; ++i)
        for (int j = i + 1; j < obj->size; ++j)
            if (obj->numbers[i] + obj->numbers[j] == value) return true;
    return false;
}
void twoSumFree(TwoSum* obj) { free(obj->numbers); free(obj); }