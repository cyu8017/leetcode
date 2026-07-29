// LeetCode 1128 - Number of Equivalent Domino Pairs
// https://leetcode.com/problems/number-of-equivalent-domino-pairs/

int numEquivDominoPairs(int** dominoes, int dominoesSize, int* dominoesColSize) {
    (void)dominoesColSize;
    int count[100] = {0};
    int ans = 0;
    for (int i = 0; i < dominoesSize; i++) {
        int a = dominoes[i][0], b = dominoes[i][1];
        if (a > b) { int t = a; a = b; b = t; }
        int key = a * 10 + b;
        ans += count[key];
        count[key]++;
    }
    return ans;
}
