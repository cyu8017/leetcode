// LeetCode 1131 - Maximum of Absolute Value Expression
// https://leetcode.com/problems/maximum-of-absolute-value-expression/

int maxAbsValExpr(int* arr1, int arr1Size, int* arr2, int arr2Size) {
    (void)arr2Size;
    int ans = 0;
    int signs[4][2] = {{1,1},{1,-1},{-1,1},{-1,-1}};
    for (int s = 0; s < 4; s++) {
        int p = signs[s][0], q = signs[s][1];
        int best = p * arr1[0] + q * arr2[0];
        for (int i = 1; i < arr1Size; i++) {
            int cur = p * arr1[i] + q * arr2[i] + i;
            if (cur - best > ans) ans = cur - best;
            int val = p * arr1[i] + q * arr2[i] + i;
            if (val < best) best = val;
        }
    }
    return ans;
}
