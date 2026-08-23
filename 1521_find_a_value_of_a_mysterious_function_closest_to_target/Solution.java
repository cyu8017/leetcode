// LeetCode 1521 - Find a Value of a Mysterious Function Closest to Target
// https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/

import java.util.*;

class Solution {
    public int closestToTarget(int[] arr, int target) {
        int answer = Integer.MAX_VALUE;
        Set<Integer> current = new HashSet<>();
        for (int value : arr) {
            Set<Integer> next = new HashSet<>();
            next.add(value);
            for (int previous : current) {
                next.add(value & previous);
            }
            current = next;
            for (int candidate : current) {
                answer = Math.min(answer, Math.abs(candidate - target));
            }
        }
        return answer;
    }
}
