// LeetCode 2512 - Reward Top K Students
// https://leetcode.com/problems/reward-top-k-students/

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int[] topStudents(String[] positive_feedback, String[] negative_feedback,
                             String[] report, int[] student_id, int k) {
        Set<String> pos = new HashSet<>(Arrays.asList(positive_feedback));
        Set<String> neg = new HashSet<>(Arrays.asList(negative_feedback));
        int[][] arr = new int[report.length][2];
        for (int i = 0; i < report.length; i++) {
            int score = 0;
            for (String w : report[i].split(" ")) {
                if (w.isEmpty()) continue;
                if (pos.contains(w)) score += 3;
                else if (neg.contains(w)) score--;
            }
            arr[i][0] = student_id[i];
            arr[i][1] = score;
        }
        Arrays.sort(arr, (a, b) -> a[1] != b[1] ? Integer.compare(b[1], a[1]) : Integer.compare(a[0], b[0]));
        int[] ans = new int[k];
        for (int i = 0; i < k; i++) ans[i] = arr[i][0];
        return ans;
    }
}
