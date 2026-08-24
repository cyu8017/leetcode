<?php
// LeetCode 2284 - Sender With Largest Word Count
// https://leetcode.com/problems/sender-with-largest-word-count/

class Solution {
    function largestWordCount($messages, $senders) {
        $count = [];
        $best = '';
        $bestCnt = -1;
        for ($i = 0; $i < count($messages); $i++) {
            $words = 1;
            $n = strlen($messages[$i]);
            for ($j = 0; $j < $n; $j++) if ($messages[$i][$j] === ' ') $words++;
            $c2 = ($count[$senders[$i]] ?? 0) + $words;
            $count[$senders[$i]] = $c2;
            if ($c2 > $bestCnt || ($c2 === $bestCnt && $senders[$i] > $best)) {
                $bestCnt = $c2;
                $best = $senders[$i];
            }
        }
        return $best;
    }
}
