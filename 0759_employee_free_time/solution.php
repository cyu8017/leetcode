<?php
// LeetCode 0759 - Employee Free Time
// https://leetcode.com/problems/employee-free-time/

class Solution {
    function employeeFreeTime($schedule) {
        $intervals = [];
        foreach ($schedule as $employee)
            foreach ($employee as $item)
                $intervals[] = [$item[0], $item[1]];
        usort($intervals, function ($a, $b) { return $a[0] - $b[0]; });
        $merged = [];
        foreach ($intervals as $iv) {
            if (count($merged) === 0 || $merged[count($merged) - 1][1] < $iv[0]) $merged[] = $iv;
            else $merged[count($merged) - 1][1] = max($merged[count($merged) - 1][1], $iv[1]);
        }
        $result = [];
        for ($i = 1; $i < count($merged); $i++)
            $result[] = [$merged[$i - 1][1], $merged[$i][0]];
        return $result;
    }
}
