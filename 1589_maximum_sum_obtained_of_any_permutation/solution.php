<?php

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer[][] $requests
     * @return Integer
     */
    function maxSumRangeQuery($nums, $requests) {
        $mod = 1000000007;
        $n = count($nums);
        $diff = array_fill(0, $n + 1, 0);
        foreach ($requests as $req) {
            $diff[$req[0]]++;
            $diff[$req[1] + 1]--;
        }
        for ($i = 1; $i < $n; $i++) {
            $diff[$i] += $diff[$i - 1];
        }
        array_pop($diff);
        sort($nums);
        sort($diff);
        $answer = 0;
        for ($i = 0; $i < $n; $i++) {
            $answer = ($answer + $nums[$i] * $diff[$i]) % $mod;
        }
        return $answer;
    }
}
