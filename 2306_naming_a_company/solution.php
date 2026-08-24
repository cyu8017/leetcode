<?php
// LeetCode 2306 - Naming a Company
// https://leetcode.com/problems/naming-a-company/

class Solution {
    function distinctNames($ideas) {
        $groups = array_fill(0, 26, []);
        foreach ($ideas as $idea) {
            $idx = ord($idea[0]) - 97;
            $groups[$idx][substr($idea, 1)] = true;
        }
        $ans = 0;
        for ($i = 0; $i < 26; ++$i) {
            for ($j = $i + 1; $j < 26; ++$j) {
                $overlap = 0;
                foreach ($groups[$i] as $s => $_) {
                    if (isset($groups[$j][$s])) $overlap++;
                }
                $ans += (count($groups[$i]) - $overlap) * (count($groups[$j]) - $overlap) * 2;
            }
        }
        return $ans;
    }
}
