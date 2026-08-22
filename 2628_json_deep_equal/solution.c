// LeetCode 2628 - JSON Deep Equal
// https://leetcode.com/problems/json-deep-equal/

#include <stdbool.h>
#include <string.h>

// JavaScript problem; C stand-in compares C strings.
bool areDeeplyEqual(const char* o1, const char* o2) {
    if (o1 == NULL || o2 == NULL) return o1 == o2;
    return strcmp(o1, o2) == 0;
}
