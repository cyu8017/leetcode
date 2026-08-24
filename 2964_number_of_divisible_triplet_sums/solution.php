<?php
// LeetCode 2964 - Number of Divisible Triplet Sums
// https://leetcode.com/problems/number-of-divisible-triplet-sums/

class Solution {
    function divisibleTripletCount($nums, $d) {
        $n = count($nums);
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $freq = [];
            for ($j = $i + 1; $j < $n; $j++) {
                $need = ($d - ($nums[$i] + $nums[$j]) % $d) % $d;
                $ans += $freq[$need] ?? 0;
                $key = $nums[$j] % $d;
                $freq[$key] = ($freq[$key] ?? 0) + 1;
            }
        }
        return $ans;
    }
}
