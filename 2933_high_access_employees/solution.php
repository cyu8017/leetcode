<?php
// LeetCode 2933 - High-Access Employees
// https://leetcode.com/problems/high-access-employees/

class Solution {
    function findHighAccessEmployees($access_times) {
        $m = [];
        foreach ($access_times as $at) {
            $name = $at[0];
            $t = $at[1];
            $hh = (ord($t[0]) - 48) * 10 + (ord($t[1]) - 48);
            $mm = (ord($t[2]) - 48) * 10 + (ord($t[3]) - 48);
            if (!isset($m[$name])) $m[$name] = [];
            $m[$name][] = $hh * 60 + $mm;
        }
        $ans = [];
        foreach ($m as $name => $times) {
            sort($times);
            $len = count($times);
            for ($i = 0; $i + 2 < $len; $i++) {
                if ($times[$i + 2] - $times[$i] < 60) {
                    $ans[] = $name;
                    break;
                }
            }
        }
        sort($ans);
        return $ans;
    }
}
