<?php
class Solution {
    function numTeams($rating) {
        $ans = 0;
        $n = count($rating);
        for ($j = 0; $j < $n; $j++) {
            $x = $rating[$j];
            $ll = 0;
            for ($i = 0; $i < $j; $i++) if ($rating[$i] < $x) $ll++;
            $lg = $j - $ll;
            $rg = 0;
            for ($i = $j + 1; $i < $n; $i++) if ($rating[$i] > $x) $rg++;
            $rl = $n - $j - 1 - $rg;
            $ans += $ll * $rg + $lg * $rl;
        }
        return $ans;
    }
}
