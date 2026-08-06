<?php
class Solution {
    function minSteps($s, $t) {
        $count = array_fill(0, 26, 0);
        for ($i = 0; $i < strlen($s); $i++) {
            $count[ord($s[$i]) - 97]++;
            $count[ord($t[$i]) - 97]--;
        }
        $answer = 0;
        foreach ($count as $c) if ($c > 0) $answer += $c;
        return $answer;
    }
}
