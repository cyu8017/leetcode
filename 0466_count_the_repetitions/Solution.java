// LeetCode 0466 - Count The Repetitions
// https://leetcode.com/problems/count-the-repetitions/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int getMaxRepetitions(String s1, int n1, String s2, int n2) {
        if (s2.isEmpty()) {
            return 0;
        }

        int index = 0;
        int s2Count = 0;
        Map<Integer, int[]> record = new HashMap<>();

        for (int repeat = 0; repeat < n1; repeat++) {
            for (int charIndex = 0; charIndex < s1.length(); charIndex++) {
                if (s1.charAt(charIndex) == s2.charAt(index)) {
                    index++;
                    if (index == s2.length()) {
                        index = 0;
                        s2Count++;
                    }
                }
            }
            if (record.containsKey(index)) {
                int[] previous = record.get(index);
                int previousRepeat = previous[0];
                int previousCount = previous[1];
                int cycle = repeat - previousRepeat;
                int countCycle = s2Count - previousCount;
                int remaining = n1 - repeat - 1;
                s2Count += (remaining / cycle) * countCycle;
                if (repeat + (remaining / cycle) * cycle >= n1 - 1) {
                    break;
                }
            }
            record.put(index, new int[] {repeat, s2Count});
        }

        return s2Count / n2;
    }
}
