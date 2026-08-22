// LeetCode 2170 - Minimum Operations to Make the Array Alternating
// https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/

#include <stdlib.h>

int minimumOperations(int* nums, int numsSize) {
    if (numsSize == 1) return 0;
    int maxv = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] > maxv) maxv = nums[i];
    int* ef = (int*)calloc((size_t)maxv + 1, sizeof(int));
    int* of = (int*)calloc((size_t)maxv + 1, sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        if (i % 2 == 0) ef[nums[i]]++;
        else of[nums[i]]++;
    }
    int e1 = 0, ec1 = 0, e2 = 0, ec2 = 0;
    int o1 = 0, oc1 = 0, o2 = 0, oc2 = 0;
    for (int v = 0; v <= maxv; v++) {
        if (ef[v] > ec1) { e2 = e1; ec2 = ec1; e1 = v; ec1 = ef[v]; }
        else if (ef[v] > ec2) { e2 = v; ec2 = ef[v]; }
        if (of[v] > oc1) { o2 = o1; oc2 = oc1; o1 = v; oc1 = of[v]; }
        else if (of[v] > oc2) { o2 = v; oc2 = of[v]; }
    }
    free(ef); free(of);
    if (e1 != o1) return numsSize - ec1 - oc1;
    int a = numsSize - ec1 - oc2;
    int b = numsSize - ec2 - oc1;
    return a < b ? a : b;
}
