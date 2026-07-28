// LeetCode 1057 - Campus Bikes
// https://leetcode.com/problems/campus-bikes/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] assignBikes(int[][] workers, int[][] bikes) {
        List<int[]> triples = new ArrayList<>();
        for (int w = 0; w < workers.length; w++) {
            for (int b = 0; b < bikes.length; b++) {
                int d = Math.abs(workers[w][0] - bikes[b][0]) + Math.abs(workers[w][1] - bikes[b][1]);
                triples.add(new int[] { d, w, b });
            }
        }
        triples.sort((a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            if (a[1] != b[1]) return Integer.compare(a[1], b[1]);
            return Integer.compare(a[2], b[2]);
        });
        int[] ans = new int[workers.length];
        for (int i = 0; i < ans.length; i++) {
            ans[i] = -1;
        }
        boolean[] usedBikes = new boolean[bikes.length];
        int assigned = 0;
        for (int[] t : triples) {
            if (ans[t[1]] == -1 && !usedBikes[t[2]]) {
                ans[t[1]] = t[2];
                usedBikes[t[2]] = true;
                assigned++;
                if (assigned == workers.length) {
                    break;
                }
            }
        }
        return ans;
    }
}
