// LeetCode 2868 - The Wording Game
// https://leetcode.com/problems/the-wording-game/

#include <stdbool.h>
#include <string.h>

bool canAliceWin(char** a, int aSize, char** b, int bSize) {
    int i = 0, j = 0;
    char last = 0;
    bool alice = true;
    for (;;) {
        if (alice) {
            while (i < aSize && a[i][0] <= last) i++;
            if (i == aSize) return false;
            last = a[i][strlen(a[i]) - 1];
            i++;
        } else {
            while (j < bSize && b[j][0] <= last) j++;
            if (j == bSize) return true;
            last = b[j][strlen(b[j]) - 1];
            j++;
        }
        alice = !alice;
    }
}
