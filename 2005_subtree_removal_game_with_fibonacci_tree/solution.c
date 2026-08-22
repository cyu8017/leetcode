// LeetCode 2005 - Subtree Removal Game with Fibonacci Tree
// https://leetcode.com/problems/subtree-removal-game-with-fibonacci-tree/

#include <stdbool.h>

bool findGameWinner(int n) {
    return n % 6 != 1;
}
