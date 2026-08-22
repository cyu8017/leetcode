// LeetCode 0168 - Excel Sheet Column Title
#include <stdlib.h>
char* convertToTitle(int columnNumber) {
    char* result = malloc(8);
    int length = 0;
    while (columnNumber) {
        --columnNumber;
        result[length++] = 'A' + columnNumber % 26;
        columnNumber /= 26;
    }
    for (int i = 0; i < length / 2; ++i) {
        char temp = result[i]; result[i] = result[length - 1 - i]; result[length - 1 - i] = temp;
    }
    result[length] = '\0';
    return result;
}