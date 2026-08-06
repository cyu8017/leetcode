<?php
class Solution {
    function distinctEchoSubstrings($text) {
        $n = strlen($text);
        $mod1 = 1000000007;
        $mod2 = 1000000009;
        $base = 911382323;
        $h1 = array_fill(0, $n + 1, 0);
        $h2 = array_fill(0, $n + 1, 0);
        $p1 = array_fill(0, $n + 1, 1);
        $p2 = array_fill(0, $n + 1, 1);
        for ($i = 0; $i < $n; $i++) {
            $code = ord($text[$i]);
            $h1[$i + 1] = ($h1[$i] * $base + $code) % $mod1;
            $h2[$i + 1] = ($h2[$i] * $base + $code) % $mod2;
            $p1[$i + 1] = ($p1[$i] * $base) % $mod1;
            $p2[$i + 1] = ($p2[$i] * $base) % $mod2;
        }
        $hashed = function($left, $right) use ($h1, $h2, $p1, $p2, $mod1, $mod2) {
            $length = $right - $left;
            return [
                (($h1[$right] - $h1[$left] * $p1[$length]) % $mod1 + $mod1) % $mod1,
                (($h2[$right] - $h2[$left] * $p2[$length]) % $mod2 + $mod2) % $mod2,
            ];
        };
        $echoes = [];
        for ($half = 1; $half <= intdiv($n, 2); $half++) {
            for ($left = 0; $left <= $n - 2 * $half; $left++) {
                $a = $hashed($left, $left + $half);
                $b = $hashed($left + $half, $left + 2 * $half);
                if ($a[0] === $b[0] && $a[1] === $b[1]) {
                    $full = $hashed($left, $left + 2 * $half);
                    $echoes[(2 * $half) . "," . $full[0] . "," . $full[1]] = true;
                }
            }
        }
        return count($echoes);
    }
}
