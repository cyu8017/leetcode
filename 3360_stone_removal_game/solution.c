// LeetCode 3360 - Stone Removal Game
// https://leetcode.com/problems/stone-removal-game/

#include <stdbool.h>

bool canAliceWin(int n) {
    int take = 10;
    int alice = 1;
    while (n >= take && take > 0) {
        n -= take;
        take--;
        alice = !alice;
    }
    return !alice;
}
