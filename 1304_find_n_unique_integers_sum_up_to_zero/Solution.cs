// LeetCode 1304 - Find N Unique Integers Sum Up To Zero
// https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

public class Solution {
    public int[] SumZero(int n) {
        var answer = new int[n];
        int idx = 0;
        for (int value = 1; value <= n / 2; value++) {
            answer[idx++] = -value;
            answer[idx++] = value;
        }
        if (n % 2 == 1) answer[idx] = 0;
        return answer;
    }
}
