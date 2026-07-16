// LeetCode 0405 - Convert a Number to Hexadecimal
// https://leetcode.com/problems/convert-a-number-to-hexadecimal/

#include <stdlib.h>
#include <string.h>

char* toHex(int num) {
    if (num == 0) {
        return strdup("0");
    }

    static const char digits[] = "0123456789abcdef";
    unsigned int value = (unsigned int)num;
    char buffer[9];
    int length = 0;

    while (value) {
        buffer[length++] = digits[value & 15];
        value >>= 4;
    }

    char* result = (char*)malloc((size_t)length + 1);
    for (int index = 0; index < length; index++) {
        result[index] = buffer[length - 1 - index];
    }
    result[length] = '\0';
    return result;
}
