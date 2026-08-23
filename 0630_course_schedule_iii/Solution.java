// LeetCode 0630 - Course Schedule III
// https://leetcode.com/problems/course-schedule-iii/

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int scheduleCourse(int[][] courses) {
        Arrays.sort(courses, (a, b) -> Integer.compare(a[1], b[1]));
        PriorityQueue<Integer> heap = new PriorityQueue<>((a, b) -> Integer.compare(b, a));
        int time = 0;
        for (int[] course : courses) {
            int duration = course[0];
            int lastDay = course[1];
            if (time + duration <= lastDay) {
                heap.offer(duration);
                time += duration;
            } else if (!heap.isEmpty() && heap.peek() > duration) {
                time += duration - heap.poll();
                heap.offer(duration);
            }
        }
        return heap.size();
    }
}
