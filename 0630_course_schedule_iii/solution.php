<?php
// LeetCode 0630 - Course Schedule III
// https://leetcode.com/problems/course-schedule-iii/

class Solution {
    function scheduleCourse($courses) {
        usort($courses, function($a, $b) { return $a[1] <=> $b[1]; });
        $heap = [];
        $push = function($v) use (&$heap) {
            $heap[] = $v;
            $i = count($heap) - 1;
            while ($i > 0) {
                $p = ($i - 1) >> 1;
                if ($heap[$p] >= $heap[$i]) break;
                $tmp = $heap[$p]; $heap[$p] = $heap[$i]; $heap[$i] = $tmp;
                $i = $p;
            }
        };
        $pop = function() use (&$heap) {
            $top = $heap[0];
            $last = array_pop($heap);
            if ($heap) {
                $heap[0] = $last;
                $i = 0;
                while (true) {
                    $largest = $i;
                    $l = $i * 2 + 1;
                    $r = $i * 2 + 2;
                    if ($l < count($heap) && $heap[$l] > $heap[$largest]) $largest = $l;
                    if ($r < count($heap) && $heap[$r] > $heap[$largest]) $largest = $r;
                    if ($largest === $i) break;
                    $tmp = $heap[$i]; $heap[$i] = $heap[$largest]; $heap[$largest] = $tmp;
                    $i = $largest;
                }
            }
            return $top;
        };
        $time = 0;
        foreach ($courses as $course) {
            $duration = $course[0];
            $lastDay = $course[1];
            if ($time + $duration <= $lastDay) {
                $push($duration);
                $time += $duration;
            } elseif ($heap && $heap[0] > $duration) {
                $time += $duration - $pop();
                $push($duration);
            }
        }
        return count($heap);
    }
}
