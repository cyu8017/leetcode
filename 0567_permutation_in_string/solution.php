<?php
// LeetCode 0567 - Permutation in String
// https://leetcode.com/problems/permutation-in-string/

class Solution {
    function checkInclusion($s1, $s2) {
        $n1 = strlen($s1);
        $n2 = strlen($s2);
        if ($n1 > $n2) return false;
        $need = array_fill(0, 26, 0);
        $window = array_fill(0, 26, 0);
        for ($i = 0; $i < $n1; ++$i) {
            ++$need[ord($s1[$i]) - 97];
            ++$window[ord($s2[$i]) - 97];
        }
        $matches = 0;
        for ($i = 0; $i < 26; ++$i) if ($need[$i] === $window[$i]) ++$matches;
        if ($matches === 26) return true;
        for ($right = $n1; $right < $n2; ++$right) {
            $add = ord($s2[$right]) - 97;
            $remove = ord($s2[$right - $n1]) - 97;
            if ($window[$add] === $need[$add]) --$matches;
            ++$window[$add];
            if ($window[$add] === $need[$add]) ++$matches;
            if ($window[$remove] === $need[$remove]) --$matches;
            --$window[$remove];
            if ($window[$remove] === $need[$remove]) ++$matches;
            if ($matches === 26) return true;
        }
        return false;
    }
}
