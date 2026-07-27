// LeetCode 1625 - Lexicographically Smallest String After Applying Operations
// https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

import java.util.*;

class Solution {
    public String findLexSmallestString(String s, int a, int b) {
        Set<String> seen = new HashSet<>();
        Queue<String> q = new ArrayDeque<>();
        seen.add(s);
        q.offer(s);
        String ans = s;
        while (!q.isEmpty()) {
            String cur = q.poll();
            if (cur.compareTo(ans) < 0) ans = cur;
            char[] chars = cur.toCharArray();
            for (int i = 1; i < chars.length; i += 2) {
                chars[i] = (char) ('0' + (chars[i] - '0' + a) % 10);
            }
            String add = new String(chars);
            String rot = cur.substring(cur.length() - b) + cur.substring(0, cur.length() - b);
            for (String nxt : new String[] {add, rot}) {
                if (seen.add(nxt)) q.offer(nxt);
            }
        }
        return ans;
    }
}
