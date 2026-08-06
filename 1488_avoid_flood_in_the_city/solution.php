<?php
class Solution {
    function avoidFlood($rains) {
        $n = count($rains);
        $ans = array_fill(0, $n, -1);
        $full = [];
        $dry = [];
        foreach ($rains as $i => $lake) {
            if ($lake === 0) {
                $dry[] = $i;
                $ans[$i] = 1;
            } else {
                if (isset($full[$lake])) {
                    $found = -1;
                    foreach ($dry as $di => $day) {
                        if ($day > $full[$lake]) {
                            $found = $di;
                            break;
                        }
                    }
                    if ($found === -1) return [];
                    $ans[$dry[$found]] = $lake;
                    array_splice($dry, $found, 1);
                }
                $full[$lake] = $i;
            }
        }
        return $ans;
    }
}
