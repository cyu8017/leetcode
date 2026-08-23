// LeetCode 2813 - Maximum Elegance of a K-Length Subsequence
// https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public long findMaximumElegance(int[][] items, int k) {
        Arrays.sort(items, (a, b) -> Integer.compare(b[0], a[0]));
        Set<Integer> seen = new HashSet<>();
        long total = 0;
        List<Integer> dup = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            total += items[i][0];
            int c = items[i][1];
            if (seen.contains(c)) dup.add(items[i][0]);
            else seen.add(c);
        }
        long ans = total + 1L * seen.size() * seen.size();
        for (int i = k; i < items.length; i++) {
            int c = items[i][1];
            if (seen.contains(c) || dup.isEmpty()) continue;
            total += items[i][0] - dup.get(dup.size() - 1);
            dup.remove(dup.size() - 1);
            seen.add(c);
            ans = Math.max(ans, total + 1L * seen.size() * seen.size());
        }
        return ans;
    }
}
