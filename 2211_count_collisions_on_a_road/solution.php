<?php
// LeetCode 2211 - Count Collisions on a Road
// https://leetcode.com/problems/count-collisions-on-a-road/

class Solution {
    function countCollisions($directions) {
        $i = 0;
        $j = strlen($directions) - 1;
        $n = strlen($directions);
        while ($i < $n && $directions[$i] === 'L') $i++;
        while ($j >= 0 && $directions[$j] === 'R') $j--;
        $ans = 0;
        for ($k = $i; $k <= $j; $k++) if ($directions[$k] !== 'S') $ans++;
        return $ans;
    }
}
