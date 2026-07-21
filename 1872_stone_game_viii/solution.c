// LeetCode 1872 - Stone Game VIII
// https://leetcode.com/problems/stone-game-viii/

int stoneGameVIII(int* stones, int stonesSize) {
    for (int i = 1; i < stonesSize; i++) stones[i] += stones[i - 1];
    int score = stones[stonesSize - 1];
    for (int i = stonesSize - 2; i > 0; i--) {
        int candidate = stones[i] - score;
        if (candidate > score) score = candidate;
    }
    return score;
}
