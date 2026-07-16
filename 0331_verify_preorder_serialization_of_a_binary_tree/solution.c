// LeetCode 0331 - Verify Preorder Serialization of a Binary Tree
// https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

#include <stdbool.h>

bool isValidSerialization(char* preorder) {
    int slots = 1;
    for (int index = 0; preorder[index] != '\0'; ) {
        int end = index;
        while (preorder[end] != ',' && preorder[end] != '\0') {
            end += 1;
        }
        slots -= 1;
        if (slots < 0) {
            return false;
        }
        if (end - index != 1 || preorder[index] != '#') {
            slots += 2;
        }
        if (preorder[end] == '\0') {
            break;
        }
        index = end + 1;
    }
    return slots == 0;
}
