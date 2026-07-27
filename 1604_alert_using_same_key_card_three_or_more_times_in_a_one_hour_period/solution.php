<?php
// LeetCode 1604 - Alert Using Same Key-Card Three or More Times in a One Hour Period
// https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

class Solution {
    /**
     * @param String[] $keyName
     * @param String[] $keyTime
     * @return String[]
     */
    function alertNames($keyName, $keyTime) {
        $times = [];
        $n = count($keyName);
        for ($i = 0; $i < $n; $i++) {
            [$h, $m] = array_map('intval', explode(':', $keyTime[$i]));
            $times[$keyName[$i]][] = $h * 60 + $m;
        }
        $ans = [];
        foreach ($times as $name => $a) {
            sort($a);
            $len = count($a);
            for ($i = 0; $i + 2 < $len; $i++) {
                if ($a[$i + 2] - $a[$i] <= 60) {
                    $ans[] = $name;
                    break;
                }
            }
        }
        sort($ans);
        return $ans;
    }
}
