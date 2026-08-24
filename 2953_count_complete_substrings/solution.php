<?php
// LeetCode 2953 - Count Complete Substrings
// https://leetcode.com/problems/count-complete-substrings/

class Solution {
    function countCompleteSubstrings($word, $k) {
        $n = strlen($word);
        $ans = 0;
        for ($i = 0; $i < $n; ) {
            $j = $i;
            while ($j + 1 < $n && abs(ord($word[$j + 1]) - ord($word[$j])) <= 2) $j++;
            $seg = substr($word, $i, $j - $i + 1);
            $m = strlen($seg);
            for ($chars = 1; $chars <= 26; $chars++) {
                $length = $chars * $k;
                if ($length > $m) break;
                $freq = array_fill(0, 26, 0);
                $unique = 0;
                for ($r = 0; $r < $m; $r++) {
                    $c = ord($seg[$r]) - 97;
                    $freq[$c]++;
                    if ($freq[$c] === 1) $unique++;
                    if ($r >= $length) {
                        $c2 = ord($seg[$r - $length]) - 97;
                        $freq[$c2]--;
                        if ($freq[$c2] === 0) $unique--;
                    }
                    if ($r >= $length - 1 && $unique === $chars) {
                        $ok = true;
                        foreach ($freq as $f) {
                            if ($f !== 0 && $f !== $k) { $ok = false; break; }
                        }
                        if ($ok) $ans++;
                    }
                }
            }
            $i = $j + 1;
        }
        return $ans;
    }
}
