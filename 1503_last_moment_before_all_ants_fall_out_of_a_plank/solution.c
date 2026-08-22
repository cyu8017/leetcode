// LeetCode 1503 - Last Moment Before All Ants Fall Out of a Plank
// https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

int getLastMoment(int n, int* left, int leftSize, int* right, int rightSize) {
    int ans = 0;
    for (int i = 0; i < leftSize; i++) {
        if (left[i] > ans) ans = left[i];
    }
    for (int i = 0; i < rightSize; i++) {
        int t = n - right[i];
        if (t > ans) ans = t;
    }
    return ans;
}
