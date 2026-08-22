// LeetCode 2038 - Remove Colored Pieces if Both Neighbors are the Same Color
// https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

#include <stdbool.h>
#include <string.h>

bool winnerOfGame(char* colors) {
    int a = 0, b = 0, n = (int)strlen(colors);
    for (int i = 1; i + 1 < n; i++) {
        if (colors[i - 1] == colors[i] && colors[i] == colors[i + 1]) {
            if (colors[i] == 'A') a++; else b++;
        }
    }
    return a > b;
}
