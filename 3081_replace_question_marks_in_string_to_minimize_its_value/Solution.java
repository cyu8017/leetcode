// LeetCode 3081 - Replace Question Marks in String to Minimize Its Value
// https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public String minimizeStringValue(String s) {
        int[] cnt = new int[26];
        int k = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '?') k++;
            else cnt[c - 'a']++;
        }
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
        for (int i = 0; i < 26; i++) pq.offer(new int[]{cnt[i], i});
        int[] t = new int[k];
        for (int i = 0; i < k; i++) {
            int[] p = pq.poll();
            t[i] = p[1];
            p[0]++;
            pq.offer(p);
        }
        Arrays.sort(t);
        char[] arr = s.toCharArray();
        int j = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == '?') {
                arr[i] = (char) (t[j] + 'a');
                j++;
            }
        }
        return new String(arr);
    }
}
