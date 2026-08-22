// LeetCode 2347 - Best Poker Hand
// https://leetcode.com/problems/best-poker-hand/

#include <stdlib.h>
#include <string.h>

char* bestHand(int* ranks, int ranksSize, char* suits, int suitsSize) {
    (void)ranksSize; (void)suitsSize;
    if (suits[0] == suits[1] && suits[1] == suits[2] && suits[2] == suits[3] && suits[3] == suits[4]) {
        char* s = (char*)malloc(6); strcpy(s, "Flush"); return s;
    }
    int cnt[14] = {0}, best = 0;
    for (int i = 0; i < 5; i++) {
        cnt[ranks[i]]++;
        if (cnt[ranks[i]] > best) best = cnt[ranks[i]];
    }
    char* s = (char*)malloc(20);
    if (best >= 3) strcpy(s, "Three of a Kind");
    else if (best == 2) strcpy(s, "Pair");
    else strcpy(s, "High Card");
    return s;
}
