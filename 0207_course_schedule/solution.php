// LeetCode 0207 - Course Schedule
// https://leetcode.com/problems/course-schedule/

class Solution {
    function canFinish($numCourses, $prerequisites) {
        $graph = array_fill(0, $numCourses, []);
        $indegree = array_fill(0, $numCourses, 0);
        foreach ($prerequisites as [$course, $prerequisite]) {
            $graph[$prerequisite][] = $course;
            $indegree[$course]++;
        }
        $queue = [];
        for ($course = 0; $course < $numCourses; $course++) {
            if ($indegree[$course] === 0) {
                $queue[] = $course;
            }
        }
        for ($index = 0; $index < count($queue); $index++) {
            foreach ($graph[$queue[$index]] as $next) {
                $indegree[$next]--;
                if ($indegree[$next] === 0) {
                    $queue[] = $next;
                }
            }
        }
        return count($queue) === $numCourses;
    }
}