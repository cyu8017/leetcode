// LeetCode 3113 - Find the Number of Subarrays Where Boundary Elements Are Maximum
// https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public long numberOfSubarrays(int[] nums) {
        Deque<int[]> stk = new ArrayDeque<>();
        long ans = 0;
        for (int x : nums) {
            while (!stk.isEmpty() && stk.peekLast()[0] < x) stk.pollLast();
            if (stk.isEmpty() || stk.peekLast()[0] > x) stk.addLast(new int[]{x, 1});
            else stk.peekLast()[1]++;
            ans += stk.peekLast()[1];
        }
        return ans;
    }
}
