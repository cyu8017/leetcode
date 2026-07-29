// LeetCode 0697 - Degree of an Array
// https://leetcode.com/problems/degree-of-an-array/

#include <limits.h>

int findShortestSubArray(int* nums, int numsSize) {
    int first[50000], last[50000], count[50000];
    for (int i = 0; i < 50000; i++) { first[i] = -1; count[i] = 0; }
    int degree = 0;
    for (int i = 0; i < numsSize; i++) {
        int v = nums[i];
        if (first[v] < 0) first[v] = i;
        last[v] = i;
        count[v]++;
        if (count[v] > degree) degree = count[v];
    }
    int best = INT_MAX;
    for (int v = 0; v < 50000; v++) {
        if (count[v] == degree) {
            int len = last[v] - first[v] + 1;
            if (len < best) best = len;
        }
    }
    return best;
}
