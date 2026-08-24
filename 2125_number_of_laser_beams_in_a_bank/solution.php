<?php
// LeetCode 2125 - Number of Laser Beams in a Bank
// https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution {
    /**
     * @param String[] $bank
     * @return Integer
     */
    function numberOfBeams($bank) {
        $ans = 0;
        $prev = 0;
        foreach ($bank as $row) {
            $cnt = 0;
            $len = strlen($row);
            for ($i = 0; $i < $len; $i++) if ($row[$i] === '1') $cnt++;
            if ($cnt > 0) {
                $ans += $prev * $cnt;
                $prev = $cnt;
            }
        }
        return $ans;
    }
}
