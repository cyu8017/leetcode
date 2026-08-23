// LeetCode 3458 - Select K Disjoint Special Substrings
// https://leetcode.com/problems/select-k-disjoint-special-substrings/

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public boolean maxSubstringLength(String s, int k) {
        int n = s.length();
        int[] first = new int[26], last = new int[26];
        for (int i = 0; i < 26; i++) { first[i] = n; last[i] = -1; }
        for (int i = 0; i < n; i++) {
            int ci = s.charAt(i) - 'a';
            if (first[ci] == n) first[ci] = i;
            last[ci] = i;
        }
        List<int[]> segs = new ArrayList<>();
        for (int c = 0; c < 26; c++) {
            if (last[c] == -1) continue;
            int l = first[c], r = last[c];
            for (int i = l; i <= r; i++) {
                int ci = s.charAt(i) - 'a';
                if (first[ci] < l) {
                    l = first[ci];
                    i = l - 1;
                    continue;
                }
                if (last[ci] > r) r = last[ci];
            }
            if (!(l == 0 && r == n - 1)) segs.add(new int[]{l, r});
        }
        Set<Long> uniq = new HashSet<>();
        List<int[]> arr = new ArrayList<>();
        for (int[] sg : segs) {
            long key = (((long) sg[0]) << 32) | (sg[1] & 0xffffffffL);
            if (uniq.add(key)) arr.add(sg);
        }
        arr.sort((a, b) -> Integer.compare(a[1], b[1]));
        int cnt = 0, end = -1;
        for (int[] sg : arr) {
            if (sg[0] > end) {
                cnt++;
                end = sg[1];
            }
        }
        return cnt >= k;
    }
}
