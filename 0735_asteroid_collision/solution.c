// LeetCode 0735 - Asteroid Collision
// https://leetcode.com/problems/asteroid-collision/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* asteroidCollision(int* asteroids, int asteroidsSize, int* returnSize) {
    int* stack = (int*)malloc((size_t)asteroidsSize * sizeof(int));
    int top = 0;
    for (int i = 0; i < asteroidsSize; i++) {
        int asteroid = asteroids[i];
        int destroyed = 0;
        while (top > 0 && asteroid < 0 && stack[top - 1] > 0) {
            if (stack[top - 1] < -asteroid) {
                top--;
                continue;
            }
            if (stack[top - 1] == -asteroid) {
                top--;
            }
            destroyed = 1;
            break;
        }
        if (!destroyed) {
            stack[top++] = asteroid;
        }
    }
    *returnSize = top;
    return stack;
}
