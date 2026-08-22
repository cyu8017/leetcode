// LeetCode 2275 - Largest Combination With Bitwise AND Greater Than Zero
// https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

int largestCombination(int* candidates, int candidatesSize) {
    int ans = 0;
    for (int bit = 0; bit < 24; bit++) {
        int cnt = 0;
        for (int i = 0; i < candidatesSize; i++) {
            if ((candidates[i] >> bit) & 1) cnt++;
        }
        if (cnt > ans) ans = cnt;
    }
    return ans;
}
