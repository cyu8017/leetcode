// LeetCode 0299 - Bulls and Cows
// https://leetcode.com/problems/bulls-and-cows/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* getHint(char* secret, char* guess) {
    int bulls = 0;
    int secretCounts[10] = {0};
    int guessCounts[10] = {0};

    int length = (int)strlen(secret);
    for (int index = 0; index < length; index++) {
        if (secret[index] == guess[index]) {
            bulls++;
        } else {
            secretCounts[secret[index] - '0']++;
            guessCounts[guess[index] - '0']++;
        }
    }

    int cows = 0;
    for (int digit = 0; digit < 10; digit++) {
        int secretCount = secretCounts[digit];
        int guessCount = guessCounts[digit];
        cows += secretCount < guessCount ? secretCount : guessCount;
    }

    char* result = (char*)malloc(16);
    snprintf(result, 16, "%dA%dB", bulls, cows);
    return result;
}
