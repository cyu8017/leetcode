// LeetCode 0264 - Ugly Number II
// https://leetcode.com/problems/ugly-number-ii/

public class Solution {
    public int NthUglyNumber(int n) {
        var ugly = new List<int> { 1 };
        int index2 = 0;
        int index3 = 0;
        int index5 = 0;
        while (ugly.Count < n) {
            int nextUgly = Math.Min(
                ugly[index2] * 2,
                Math.Min(ugly[index3] * 3, ugly[index5] * 5)
            );
            ugly.Add(nextUgly);
            if (nextUgly == ugly[index2] * 2) {
                index2++;
            }
            if (nextUgly == ugly[index3] * 3) {
                index3++;
            }
            if (nextUgly == ugly[index5] * 5) {
                index5++;
            }
        }
        return ugly[ugly.Count - 1];
    }
}
