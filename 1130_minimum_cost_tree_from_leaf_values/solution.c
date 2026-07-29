// LeetCode 1130 - Minimum Cost Tree From Leaf Values
// https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

int mctFromLeafValues(int* arr, int arrSize) {
    int stack[505];
    int top = 0;
    stack[top++] = 1000000000;
    int ans = 0;
    for (int i = 0; i < arrSize; i++) {
        int x = arr[i];
        while (stack[top - 1] <= x) {
            int mid = stack[--top];
            int m = stack[top - 1] < x ? stack[top - 1] : x;
            ans += mid * m;
        }
        stack[top++] = x;
    }
    while (top > 2) {
        int mid = stack[--top];
        ans += mid * stack[top - 1];
    }
    return ans;
}
