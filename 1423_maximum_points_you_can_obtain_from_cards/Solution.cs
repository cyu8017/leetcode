// LeetCode 1423 - Maximum Points You Can Obtain From Cards
// https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

using System.Linq;
public class Solution {
    public int MaxScore(int[] cardPoints, int k) {
        if (k == cardPoints.Length) return cardPoints.Sum();
        int window = cardPoints.Length - k, current = 0;
        for (int i = 0; i < window; i++) current += cardPoints[i];
        int smallest = current;
        for (int i = window; i < cardPoints.Length; i++) {
            current += cardPoints[i] - cardPoints[i - window];
            smallest = System.Math.Min(smallest, current);
        }
        return cardPoints.Sum() - smallest;
    }
}
