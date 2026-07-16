// LeetCode 0166 - Fraction to Recurring Decimal
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char* fractionToDecimal(int numerator, int denominator) {
    if (!numerator) return strdup("0");
    long long n = numerator, d = denominator;
    char* result = malloc(10005);
    int length = 0;
    if ((n < 0) ^ (d < 0)) result[length++] = '-';
    n = llabs(n); d = llabs(d);
    length += sprintf(result + length, "%lld", n / d);
    long long remainder = n % d;
    if (!remainder) return result;
    result[length++] = '.';
    long long* remainders = malloc(10000 * sizeof(long long));
    int* positions = malloc(10000 * sizeof(int));
    int seenCount = 0;
    while (remainder) {
        int position = -1;
        for (int i = 0; i < seenCount; ++i)
            if (remainders[i] == remainder) { position = positions[i]; break; }
        if (position >= 0) {
            memmove(result + position + 1, result + position, length - position + 1);
            result[position] = '('; result[++length] = ')'; result[length + 1] = '\0';
            break;
        }
        remainders[seenCount] = remainder;
        positions[seenCount++] = length;
        remainder *= 10;
        result[length++] = '0' + remainder / d;
        remainder %= d;
    }
    free(remainders); free(positions);
    return result;
}