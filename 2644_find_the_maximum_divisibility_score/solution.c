// LeetCode 2644 - Find the Maximum Divisibility Score
// https://leetcode.com/problems/find-the-maximum-divisibility-score/

int maxDivScore(int* nums, int numsSize, int* divisors, int divisorsSize) {
    int best = divisors[0], bestScore = -1;
    for (int i = 0; i < divisorsSize; i++) {
        int d = divisors[i], score = 0;
        for (int j = 0; j < numsSize; j++)
            if (nums[j] % d == 0) score++;
        if (score > bestScore || (score == bestScore && d < best)) {
            bestScore = score;
            best = d;
        }
    }
    return best;
}
