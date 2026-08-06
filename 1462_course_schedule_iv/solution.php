<?php
class Solution {
    function checkIfPrerequisite($numCourses, $prerequisites, $queries) {
        $reach = array_fill(0, $numCourses, array_fill(0, $numCourses, false));
        foreach ($prerequisites as [$a, $b]) $reach[$a][$b] = true;
        for ($k = 0; $k < $numCourses; $k++) {
            for ($i = 0; $i < $numCourses; $i++) {
                if ($reach[$i][$k]) {
                    for ($j = 0; $j < $numCourses; $j++) {
                        $reach[$i][$j] = $reach[$i][$j] || $reach[$k][$j];
                    }
                }
            }
        }
        $answer = [];
        foreach ($queries as [$a, $b]) $answer[] = $reach[$a][$b];
        return $answer;
    }
}
