// LeetCode 1209 - Remove All Adjacent Duplicates in String II
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

import java.util.*;

class Solution {
    public String removeDuplicates(String s, int k) {
        Deque<int[]> stack = new ArrayDeque<>();
        for (char ch : s.toCharArray()) {
            if (!stack.isEmpty() && stack.peek()[0] == ch) stack.peek()[1]++;
            else stack.push(new int[]{ch, 1});
            if (stack.peek()[1] == k) stack.pop();
        }
        StringBuilder sb = new StringBuilder();
        List<int[]> list = new ArrayList<>(stack);
        Collections.reverse(list);
        for (int[] p : list) for (int i = 0; i < p[1]; i++) sb.append((char) p[0]);
        return sb.toString();
    }
}
