// LeetCode 0379 - Design Phone Directory
// https://leetcode.com/problems/design-phone-directory/

#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    bool* available;
    int maxNumbers;
} PhoneDirectory;

PhoneDirectory* phoneDirectoryCreate(int maxNumbers) {
    PhoneDirectory* obj = (PhoneDirectory*)malloc(sizeof(PhoneDirectory));
    obj->maxNumbers = maxNumbers;
    obj->available = (bool*)malloc((size_t)maxNumbers * sizeof(bool));
    for (int number = 0; number < maxNumbers; number++) {
        obj->available[number] = true;
    }
    return obj;
}

int phoneDirectoryGet(PhoneDirectory* obj) {
    for (int number = 0; number < obj->maxNumbers; number++) {
        if (obj->available[number]) {
            obj->available[number] = false;
            return number;
        }
    }
    return -1;
}

bool phoneDirectoryCheck(PhoneDirectory* obj, int number) {
    if (number < 0 || number >= obj->maxNumbers) {
        return false;
    }
    return obj->available[number];
}

void phoneDirectoryRelease(PhoneDirectory* obj, int number) {
    if (number >= 0 && number < obj->maxNumbers) {
        obj->available[number] = true;
    }
}

void phoneDirectoryFree(PhoneDirectory* obj) {
    free(obj->available);
    free(obj);
}
