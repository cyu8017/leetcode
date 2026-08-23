// LeetCode 0630 - Course Schedule III
// https://leetcode.com/problems/course-schedule-iii/

using System;
using System.Collections.Generic;

public class Solution {
    public int ScheduleCourse(int[][] courses) {
        Array.Sort(courses, (a, b) => a[1].CompareTo(b[1]));
        var heap = new PriorityQueue<int, int>();
        int time = 0;
        foreach (var course in courses) {
            int duration = course[0], lastDay = course[1];
            if (time + duration <= lastDay) {
                heap.Enqueue(duration, -duration);
                time += duration;
            } else if (heap.Count > 0 && heap.Peek() > duration) {
                time += duration - heap.Dequeue();
                heap.Enqueue(duration, -duration);
            }
        }
        return heap.Count;
    }
}
