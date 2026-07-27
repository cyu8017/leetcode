// LeetCode 1014 - Best Sightseeing Pair
// https://leetcode.com/problems/best-sightseeing-pair/

int maxScoreSightseeingPair(int* values, int valuesSize) {
    int best = values[0], ans = 0;
    for (int j = 1; j < valuesSize; j++) {
        int score = best + values[j] - j;
        if (score > ans) ans = score;
        int cand = values[j] + j;
        if (cand > best) best = cand;
    }
    return ans;
}
