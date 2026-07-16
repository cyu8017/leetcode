// LeetCode 0264 - Ugly Number II
// https://leetcode.com/problems/ugly-number-ii/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int nthUglyNumber(int n) {
        List<Integer> ugly = new ArrayList<>();
        ugly.add(1);
        int index2 = 0;
        int index3 = 0;
        int index5 = 0;
        while (ugly.size() < n) {
            int nextUgly = Math.min(
                ugly.get(index2) * 2,
                Math.min(ugly.get(index3) * 3, ugly.get(index5) * 5)
            );
            ugly.add(nextUgly);
            if (nextUgly == ugly.get(index2) * 2) {
                index2++;
            }
            if (nextUgly == ugly.get(index3) * 3) {
                index3++;
            }
            if (nextUgly == ugly.get(index5) * 5) {
                index5++;
            }
        }
        return ugly.get(ugly.size() - 1);
    }
}
