<?php
// LeetCode 3999 - Minimum Number of String Groups Through Transformations
// https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/

class Solution {
    function minimumGroups($words) {
        $keys = [];
        foreach ($words as $w) {
            $n = strlen($w);
            $even = '';
            $odd = '';
            for ($i = 0; $i < $n; $i++) {
                if ($i % 2 === 0) $even .= $w[$i];
                else $odd .= $w[$i];
            }
            $keys[] = $this->canonicalRotate($even) . '#' . $this->canonicalRotate($odd);
        }
        sort($keys);
        $groups = 0;
        for ($i = 0; $i < count($keys); $i++) {
            if ($i === 0 || $keys[$i] !== $keys[$i - 1]) $groups++;
        }
        return $groups;
    }

    private function leastRotation($s) {
        $n = strlen($s);
        $i = 0;
        $j = 1;
        $k = 0;
        while ($i < $n && $j < $n && $k < $n) {
            $a = $s[($i + $k) % $n];
            $b = $s[($j + $k) % $n];
            if ($a === $b) $k++;
            else {
                if ($a > $b) $i += $k + 1;
                else $j += $k + 1;
                if ($i === $j) $j++;
                $k = 0;
            }
        }
        return $i < $j ? $i : $j;
    }

    private function canonicalRotate($s) {
        $n = strlen($s);
        if ($n <= 1) return $s;
        $r = $this->leastRotation($s);
        if ($r === 0) return $s;
        return substr($s, $r) . substr($s, 0, $r);
    }
}
