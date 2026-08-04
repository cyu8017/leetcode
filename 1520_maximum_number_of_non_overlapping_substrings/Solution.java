// LeetCode 1520 - Maximum Number of Non-Overlapping Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/

import java.util.*;

class Solution {
    public List<String> maxNumOfSubstrings(String s) {
        int[] first = new int[26];
        int[] last = new int[26];
        Arrays.fill(first, -1);
        Arrays.fill(last, -1);

        for (int i = 0; i < s.length(); i++) {
            int index = s.charAt(i) - 'a';
            if (first[index] == -1) {
                first[index] = i;
            }
            last[index] = i;
        }

        List<int[]> intervals = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            int ch = s.charAt(i) - 'a';
            if (first[ch] != i) {
                continue;
            }
            int end = last[ch];
            int j = i;
            boolean valid = true;
            while (j <= end) {
                int cj = s.charAt(j) - 'a';
                if (first[cj] < i) {
                    valid = false;
                    break;
                }
                end = Math.max(end, last[cj]);
                j++;
            }
            if (valid) {
                intervals.add(new int[] { end, i });
            }
        }

        intervals.sort(Comparator.comparingInt(a -> a[0]));
        List<String> answer = new ArrayList<>();
        int previousEnd = -1;
        for (int[] interval : intervals) {
            int end = interval[0];
            int start = interval[1];
            if (start > previousEnd) {
                answer.add(s.substring(start, end + 1));
                previousEnd = end;
            }
        }

        answer.sort(Comparator.comparingInt(String::length));
        return answer;
    }
}
