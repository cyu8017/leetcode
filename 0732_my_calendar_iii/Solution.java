// LeetCode 0732 - My Calendar III
// https://leetcode.com/problems/my-calendar-iii/

import java.util.*;

class MyCalendarThree {
    private final TreeMap<Integer, Integer> delta = new TreeMap<>();

    public MyCalendarThree() {}

    public int book(int startTime, int endTime) {
        delta.put(startTime, delta.getOrDefault(startTime, 0) + 1);
        delta.put(endTime, delta.getOrDefault(endTime, 0) - 1);
        int current = 0, best = 0;
        for (int change : delta.values()) {
            current += change;
            best = Math.max(best, current);
        }
        return best;
    }
}
