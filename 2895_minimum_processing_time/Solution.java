// LeetCode 2895 - Minimum Processing Time
// https://leetcode.com/problems/minimum-processing-time/

import java.util.Collections;
import java.util.List;

class Solution {
    public int minProcessingTime(List<Integer> processorTime, List<Integer> tasks) {
        Collections.sort(processorTime);
        tasks.sort(Collections.reverseOrder());
        int ans = 0;
        for (int i = 0; i < processorTime.size(); i++) {
            int fin = processorTime.get(i) + tasks.get(i * 4);
            if (fin > ans) ans = fin;
        }
        return ans;
    }
}
