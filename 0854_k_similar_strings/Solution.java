// LeetCode 0854 - K-Similar Strings
// https://leetcode.com/problems/k-similar-strings/

import java.util.*;

class Solution {
    private String s2;

    public int kSimilarity(String s1, String s2) {
        if (s1.equals(s2)) return 0;
        this.s2 = s2;
        Queue<String> queue = new ArrayDeque<>();
        Map<String, Integer> dist = new HashMap<>();
        queue.offer(s1);
        dist.put(s1, 0);
        while (!queue.isEmpty()) {
            String cur = queue.poll();
            int d = dist.get(cur);
            for (String nxt : neighbors(cur)) {
                if (nxt.equals(s2)) return d + 1;
                if (!dist.containsKey(nxt)) {
                    dist.put(nxt, d + 1);
                    queue.offer(nxt);
                }
            }
        }
        return -1;
    }

    private List<String> neighbors(String s) {
        char[] arr = s.toCharArray();
        int i = 0;
        while (arr[i] == s2.charAt(i)) i++;
        List<String> res = new ArrayList<>();
        for (int j = i + 1; j < arr.length; j++) {
            if (arr[j] == s2.charAt(i) && arr[j] != s2.charAt(j)) {
                char tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
                res.add(new String(arr));
                arr[j] = arr[i];
                arr[i] = tmp;
            }
        }
        return res;
    }
}
