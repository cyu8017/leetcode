<?php
// LeetCode 2410 - Maximum Matching of Players With Trainers
// https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution {
    function matchPlayersAndTrainers($players, $trainers) {
        sort($players);
        sort($trainers);
        $i = 0;
        $j = 0;
        $ans = 0;
        $pn = count($players);
        $tn = count($trainers);
        while ($i < $pn && $j < $tn) {
            if ($players[$i] <= $trainers[$j]) { $ans++; $i++; $j++; }
            else $j++;
        }
        return $ans;
    }
}
