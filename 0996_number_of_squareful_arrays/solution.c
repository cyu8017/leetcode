// LeetCode 0996 - Number of Squareful Arrays
// https://leetcode.com/problems/number-of-squareful-arrays/

#include <stdlib.h>
#include <math.h>

static int keys[20], count_map[20], kn;
static int graph[20][20], gsz[20];
static int ans_g, n_g;

static int keyIndex(int x) {
    for (int i = 0; i < kn; i++) if (keys[i] == x) return i;
    return -1;
}

static int isSquare(int s) {
    int r = (int)(sqrt((double)s) + 0.5);
    return r * r == s;
}

static void dfs(int xi, int remain) {
    if (remain == 0) { ans_g++; return; }
    for (int t = 0; t < gsz[xi]; t++) {
        int yi = graph[xi][t];
        if (count_map[yi]) {
            count_map[yi]--;
            dfs(yi, remain - 1);
            count_map[yi]++;
        }
    }
}

int numSquarefulPerms(int* nums, int numsSize) {
    kn = 0; n_g = numsSize;
    for (int i = 0; i < numsSize; i++) {
        int idx = keyIndex(nums[i]);
        if (idx < 0) { keys[kn] = nums[i]; count_map[kn] = 1; kn++; }
        else count_map[idx]++;
    }
    for (int i = 0; i < kn; i++) {
        gsz[i] = 0;
        for (int j = 0; j < kn; j++) {
            if (isSquare(keys[i] + keys[j])) graph[i][gsz[i]++] = j;
        }
    }
    ans_g = 0;
    for (int i = 0; i < kn; i++) {
        count_map[i]--;
        dfs(i, numsSize - 1);
        count_map[i]++;
    }
    return ans_g;
}
