<?php
// LeetCode 3577 - Count the Number of Computer Unlocking Permutations
// https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

class Solution {
    function countPermutations($complexity) {
        $mod = 1000000007;
        $ans = 1;
        for ($i = 1; $i < count($complexity); $i++) {
            if ($complexity[$i] <= $complexity[0]) return 0;
            $ans = (int)(($ans * $i) % $mod);
        }
        return $ans;
    }
}
