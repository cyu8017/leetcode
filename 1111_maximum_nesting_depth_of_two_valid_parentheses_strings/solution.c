// LeetCode 1111 - Maximum Nesting Depth of Two Valid Parentheses Strings
// https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

#include <stdlib.h>
#include <string.h>

int* maxDepthAfterSplit(char* seq, int* returnSize) {
    int n = (int)strlen(seq);
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    int depth = 0;
    for (int i = 0; i < n; i++) {
        if (seq[i] == '(') {
            ans[i] = depth % 2;
            depth++;
        } else {
            depth--;
            ans[i] = depth % 2;
        }
    }
    *returnSize = n;
    return ans;
}
