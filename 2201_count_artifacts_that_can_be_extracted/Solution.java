// LeetCode 2201 - Count Artifacts That Can Be Extracted
// https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int digArtifacts(int n, int[][] artifacts, int[][] dig) {
        Set<Long> dug = new HashSet<>();
        for (int[] d : dig) dug.add(((long) d[0] << 32) | (d[1] & 0xffffffffL));
        int ans = 0;
        for (int[] a : artifacts) {
            boolean ok = true;
            for (int r = a[0]; r <= a[2] && ok; r++)
                for (int c = a[1]; c <= a[3]; c++)
                    if (!dug.contains(((long) r << 32) | (c & 0xffffffffL))) {
                        ok = false;
                        break;
                    }
            if (ok) ans++;
        }
        return ans;
    }
}
