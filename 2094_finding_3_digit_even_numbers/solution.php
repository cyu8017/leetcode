<?php
// LeetCode 2094 - Finding 3-Digit Even Numbers
// https://leetcode.com/problems/finding-3-digit-even-numbers/

class Solution {
    /**
     * @param Integer[] $digits
     * @return Integer[]
     */
    function findEvenNumbers($digits) {
        $freq = array_fill(0, 10, 0);
        foreach ($digits as $d) $freq[$d]++;
        $ans = [];
        for ($x = 100; $x <= 998; $x += 2) {
            $a = intdiv($x, 100);
            $b = intdiv($x, 10) % 10;
            $c = $x % 10;
            $freq[$a]--;
            $freq[$b]--;
            $freq[$c]--;
            if ($freq[$a] >= 0 && $freq[$b] >= 0 && $freq[$c] >= 0) $ans[] = $x;
            $freq[$a]++;
            $freq[$b]++;
            $freq[$c]++;
        }
        return $ans;
    }
}
