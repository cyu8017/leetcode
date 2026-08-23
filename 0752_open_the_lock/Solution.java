// LeetCode 0752 - Open the Lock
// https://leetcode.com/problems/open-the-lock/

import java.util.*;

class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> dead = new HashSet<>(Arrays.asList(deadends));
        if (dead.contains("0000")) return -1;
        Queue<String> q = new ArrayDeque<>();
        Queue<Integer> stepsQ = new ArrayDeque<>();
        Set<String> seen = new HashSet<>();
        seen.add("0000");
        q.offer("0000");
        stepsQ.offer(0);
        while (!q.isEmpty()) {
            String state = q.poll();
            int steps = stepsQ.poll();
            if (state.equals(target)) return steps;
            char[] chars = state.toCharArray();
            for (int i = 0; i < 4; i++) {
                int digit = chars[i] - '0';
                for (int delta : new int[] {-1, 1}) {
                    chars[i] = (char) ('0' + (digit + delta + 10) % 10);
                    String nxt = new String(chars);
                    chars[i] = (char) ('0' + digit);
                    if (seen.add(nxt) && !dead.contains(nxt)) {
                        q.offer(nxt);
                        stepsQ.offer(steps + 1);
                    }
                }
            }
        }
        return -1;
    }
}
