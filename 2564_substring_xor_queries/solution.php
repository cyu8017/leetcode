<?php
// LeetCode 2564 - Substring XOR Queries
// https://leetcode.com/problems/substring-xor-queries/

class Solution {
    function substringXorQueries($s, $queries) {
        $pos = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '0') {
                if (!isset($pos[0])) $pos[0] = [$i, $i];
                continue;
            }
            $val = 0;
            for ($j = $i; $j < $n && $j < $i + 30; $j++) {
                $val = $val * 2 + (ord($s[$j]) - 48);
                if (!isset($pos[$val])) $pos[$val] = [$i, $j];
            }
        }
        $ans = [];
        foreach ($queries as $q) {
            $need = $q[0] ^ $q[1];
            $ans[] = isset($pos[$need]) ? $pos[$need] : [-1, -1];
        }
        return $ans;
    }
}
