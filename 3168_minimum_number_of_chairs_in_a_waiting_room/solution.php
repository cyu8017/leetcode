<?php
// LeetCode 3168 - Minimum Number of Chairs in a Waiting Room
// https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

class Solution {
    function minimumChairs($s) {
        $cnt = 0;
        $left = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c === "E") {
                if ($left > 0) $left--;
                else $cnt++;
            } else $left++;
        }
        return $cnt;
    }
}
