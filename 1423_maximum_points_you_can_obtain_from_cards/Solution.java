// LeetCode 1423 - Maximum Points You Can Obtain From Cards
// https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int total = 0;
        for (int x : cardPoints) total += x;
        if (k == cardPoints.length) return total;
        int window = cardPoints.length - k, current = 0;
        for (int i = 0; i < window; i++) current += cardPoints[i];
        int smallest = current;
        for (int i = window; i < cardPoints.length; i++) {
            current += cardPoints[i] - cardPoints[i - window];
            smallest = Math.min(smallest, current);
        }
        return total - smallest;
    }
}
