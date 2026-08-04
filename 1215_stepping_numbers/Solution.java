// LeetCode 1215 - Stepping Numbers
// https://leetcode.com/problems/stepping-numbers/

import java.util.*;

class Solution {
    public List<Integer> countSteppingNumbers(int low, int high) {
        List<Integer> answer = new ArrayList<>();
        if (low == 0) answer.add(0);
        ArrayDeque<Integer> q = new ArrayDeque<>();
        for (int i = 1; i < 10; i++) q.add(i);
        while (!q.isEmpty()) {
            int x = q.removeFirst();
            if (x > high) continue;
            if (x >= low) answer.add(x);
            int last = x % 10;
            if (last > 0) q.add(x * 10 + last - 1);
            if (last < 9) q.add(x * 10 + last + 1);
        }
        Collections.sort(answer);
        return answer;
    }
}
