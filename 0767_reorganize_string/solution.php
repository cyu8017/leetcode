<?php
// LeetCode 0767 - Reorganize String
// https://leetcode.com/problems/reorganize-string/

class Solution {
    function reorganizeString($s) {
        $freq = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $freq[ord($s[$i]) - 97]++;
        $heap = [];
        for ($i = 0; $i < 26; $i++) {
            if ($freq[$i] > 0) $heap[] = [$freq[$i], $i];
        }
        usort($heap, function ($a, $b) { return $b[0] - $a[0]; });
        if (count($heap) > 0 && $heap[0][0] > intdiv($n + 1, 2)) return '';
        $result = '';
        while (count($heap) >= 2) {
            usort($heap, function ($a, $b) { return $b[0] - $a[0]; });
            $x = array_shift($heap);
            $y = array_shift($heap);
            $result .= chr(97 + $x[1]);
            $result .= chr(97 + $y[1]);
            if (--$x[0] > 0) $heap[] = $x;
            if (--$y[0] > 0) $heap[] = $y;
        }
        if (count($heap) > 0) $result .= chr(97 + $heap[0][1]);
        return $result;
    }
}
