// LeetCode 1753 - Maximum Score From Removing Stones
// https://leetcode.com/problems/maximum-score-from-removing-stones/

static void sortDescending3(int* stones) {
    for (int i = 0; i < 2; i++) {
        for (int j = i + 1; j < 3; j++) {
            if (stones[j] > stones[i]) {
                int tmp = stones[i];
                stones[i] = stones[j];
                stones[j] = tmp;
            }
        }
    }
}

int maximumScore(int a, int b, int c) {
    int stones[3] = { a, b, c };
    sortDescending3(stones);
    int score = 0;
    while (stones[0] > 0 && stones[1] > 0) {
        stones[0]--;
        stones[1]--;
        score++;
        sortDescending3(stones);
    }
    return score;
}
