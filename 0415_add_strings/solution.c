// LeetCode 0415 - Add Strings
// https://leetcode.com/problems/add-strings/

#include <stdlib.h>
#include <string.h>

char* addStrings(char* num1, char* num2) {
    int index1 = (int)strlen(num1) - 1;
    int index2 = (int)strlen(num2) - 1;
    int carry = 0;
    char buffer[512];
    int length = 0;

    while (index1 >= 0 || index2 >= 0 || carry) {
        if (index1 >= 0) {
            carry += num1[index1] - '0';
            index1--;
        }
        if (index2 >= 0) {
            carry += num2[index2] - '0';
            index2--;
        }
        buffer[length++] = (char)('0' + carry % 10);
        carry /= 10;
    }

    char* result = (char*)malloc((size_t)length + 1);
    for (int index = 0; index < length; index++) {
        result[index] = buffer[length - 1 - index];
    }
    result[length] = '\0';
    return result;
}
