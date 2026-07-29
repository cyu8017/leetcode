// LeetCode 1423 - Maximum Points You Can Obtain from Cards
// https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

int maxScore(int* cardPoints, int cardPointsSize, int k) {
    int total = 0;
    for (int i = 0; i < cardPointsSize; i++) total += cardPoints[i];
    if (k == cardPointsSize) return total;
    int window = cardPointsSize - k;
    int current = 0;
    for (int i = 0; i < window; i++) current += cardPoints[i];
    int smallest = current;
    for (int i = window; i < cardPointsSize; i++) {
        current += cardPoints[i] - cardPoints[i - window];
        if (current < smallest) smallest = current;
    }
    return total - smallest;
}
