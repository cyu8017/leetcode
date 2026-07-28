// LeetCode 1086 - High Five
// https://leetcode.com/problems/high-five/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[][] highFive(int[][] items) {
        Map<Integer, List<Integer>> scores = new HashMap<>();
        for (int[] item : items) {
            scores.computeIfAbsent(item[0], k -> new ArrayList<>()).add(item[1]);
        }
        List<Integer> ids = new ArrayList<>(scores.keySet());
        Collections.sort(ids);
        int[][] ans = new int[ids.size()][2];
        for (int i = 0; i < ids.size(); i++) {
            int id = ids.get(i);
            List<Integer> top = new ArrayList<>(scores.get(id));
            top.sort(Collections.reverseOrder());
            int sum = 0;
            for (int j = 0; j < 5; j++) {
                sum += top.get(j);
            }
            ans[i][0] = id;
            ans[i][1] = sum / 5;
        }
        return ans;
    }
}
