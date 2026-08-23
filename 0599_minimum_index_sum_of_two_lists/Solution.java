// LeetCode 0599 - Minimum Index Sum of Two Lists
// https://leetcode.com/problems/minimum-index-sum-of-two-lists/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        Map<String, Integer> index1 = new HashMap<>();
        for (int i = 0; i < list1.length; ++i) {
            index1.put(list1[i], i);
        }

        int best = Integer.MAX_VALUE;
        List<String> answer = new ArrayList<>();
        for (int j = 0; j < list2.length; ++j) {
            Integer i = index1.get(list2[j]);
            if (i == null) {
                continue;
            }
            int total = i + j;
            if (total < best) {
                best = total;
                answer.clear();
                answer.add(list2[j]);
            } else if (total == best) {
                answer.add(list2[j]);
            }
        }
        return answer.toArray(new String[0]);
    }
}
