// LeetCode 0483 - Smallest Good Base
// https://leetcode.com/problems/smallest-good-base/

#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int seriesEquals(unsigned long long num, int length, unsigned long long base) {
    __uint128_t total = 1;
    __uint128_t power = 1;
    for (int index = 1; index < length; index++) {
        power *= base;
        total += power;
        if (total > num) {
            return 0;
        }
    }
    return total == num;
}

char* smallestGoodBase(char* n) {
    unsigned long long num = strtoull(n, NULL, 10);
    char* answer = (char*)malloc(32);
    for (int length = (int)log2((long double)num) + 1; length >= 2; length--) {
        unsigned long long low = 2;
        unsigned long long high = num - 1;
        while (low <= high) {
            unsigned long long mid = low + (high - low) / 2;
            if (seriesEquals(num, length, mid)) {
                sprintf(answer, "%llu", mid);
                return answer;
            }
            __uint128_t total = 1;
            __uint128_t power = 1;
            int tooLarge = 0;
            for (int index = 1; index < length; index++) {
                power *= mid;
                total += power;
                if (total > num) {
                    tooLarge = 1;
                    break;
                }
            }
            if (tooLarge || total > num) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
    }
    sprintf(answer, "%llu", num - 1);
    return answer;
}
