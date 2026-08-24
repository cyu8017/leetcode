<?php
// LeetCode 3936 - Minimum Swaps To Move Zeros To End
// https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/

class Solution {
    function minimumSwaps($nums) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0, $j = $n - 1; $i < $j; $i++, $j--) {
            while ($i < $n && $nums[$i] != 0) $i++;
            while ($j > 0 && $nums[$j] == 0) $j--;
            if ($i >= $j) break;
            $ans++;
        }
        return $ans;
    }
}
