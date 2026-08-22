// LeetCode 2618 - Check if Object Instance of Class
// https://leetcode.com/problems/check-if-object-instance-of-class/

#include <stdbool.h>
#include <stddef.h>

// JavaScript problem; C stand-in mirrors Go: non-null => true.
bool checkIfInstanceOf(void* obj, void* classFunction) {
    if (obj == NULL || classFunction == NULL) return false;
    return true;
}
