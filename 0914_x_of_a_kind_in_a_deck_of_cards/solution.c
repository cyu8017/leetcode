// LeetCode 0914 - X of a Kind in a Deck of Cards
// https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

#include <stdbool.h>
#include <stdlib.h>

static int gcd(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

bool hasGroupsSizeX(int* deck, int deckSize) {
    int* counts = (int*)calloc(10001, sizeof(int));
    for (int i = 0; i < deckSize; i++) counts[deck[i]]++;
    int g = 0;
    for (int i = 0; i <= 10000; i++) {
        if (counts[i]) {
            g = g == 0 ? counts[i] : gcd(g, counts[i]);
        }
    }
    free(counts);
    return g >= 2;
}
