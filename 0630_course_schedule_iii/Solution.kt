// LeetCode 0630 - Course Schedule III
// https://leetcode.com/problems/course-schedule-iii/


class Solution {
    fun scheduleCourse(courses: Array<IntArray>): Int {
        courses.sortBy { it[1] }
        val pq = java.util.PriorityQueue<Int>(compareByDescending { it })
        var time = 0
        for (c in courses) {
            val duration = c[0]
            val last = c[1]
            if (time + duration <= last) {
                pq.add(duration)
                time += duration
            } else if (pq.isNotEmpty() && pq.peek() > duration) {
                time += duration - pq.poll()
                pq.add(duration)
            }
        }
        return pq.size
    }
}
