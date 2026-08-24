<?php
// LeetCode 0210 - Course Schedule II
// https://leetcode.com/problems/course-schedule-ii/

class Solution {
    function findOrder($numCourses, $prerequisites) {
        $graph = array_fill(0, $numCourses, []);
        $indegree = array_fill(0, $numCourses, 0);
        foreach ($prerequisites as [$course, $prerequisite]) {
            $graph[$prerequisite][] = $course;
            $indegree[$course]++;
        }
        $order = [];
        for ($course = 0; $course < $numCourses; $course++) {
            if ($indegree[$course] === 0) {
                $order[] = $course;
            }
        }
        for ($index = 0; $index < count($order); $index++) {
            foreach ($graph[$order[$index]] as $next) {
                $indegree[$next]--;
                if ($indegree[$next] === 0) {
                    $order[] = $next;
                }
            }
        }
        return count($order) === $numCourses ? $order : [];
    }
}
