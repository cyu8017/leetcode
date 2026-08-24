<?php
// LeetCode 3478 - Choose K Elements With Maximum Sum
// https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

class Solution {
    function findMaxSum($nums1, $nums2, $k) {
        $n = count($nums1);
        $arr = [];
        for ($i = 0; $i < $n; $i++) $arr[] = [$nums1[$i], $nums2[$i], $i];
        usort($arr, function($a, $b) { return $a[0] <=> $b[0]; });
        $ans = array_fill(0, $n, 0);
        $h = [];
        $sum = 0;
        $push = function($v) use (&$h) { $h[] = $v; sort($h); };
        $poll = function() use (&$h) { return array_shift($h); };
        for ($i = 0; $i < $n; ) {
            $v = $arr[$i][0];
            $start = $i;
            while ($i < $n && $arr[$i][0] === $v) $i++;
            for ($t = $start; $t < $i; $t++) $ans[$arr[$t][2]] = $sum;
            for ($t = $start; $t < $i; $t++) {
                $push($arr[$t][1]);
                $sum += $arr[$t][1];
                if (count($h) > $k) $sum -= $poll();
            }
        }
        return $ans;
    }
}
