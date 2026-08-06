<?php
class Solution {
    function numPoints($darts, $r) {
        $ans = $darts ? 1 : 0;
        $n = count($darts);
        for ($i = 0; $i < $n; $i++) {
            [$x1, $y1] = $darts[$i];
            for ($j = $i + 1; $j < $n; $j++) {
                [$x2, $y2] = $darts[$j];
                $dx = $x2 - $x1;
                $dy = $y2 - $y1;
                $d2 = $dx * $dx + $dy * $dy;
                if ($d2 > 4 * $r * $r || $d2 == 0) continue;
                $d = sqrt($d2);
                $h = sqrt($r * $r - $d2 / 4);
                $mx = ($x1 + $x2) / 2;
                $my = ($y1 + $y2) / 2;
                foreach ([-1, 1] as $sign) {
                    $cx = $mx + $sign * (-$dy) * $h / $d;
                    $cy = $my + $sign * $dx * $h / $d;
                    $count = 0;
                    foreach ($darts as [$x, $y]) {
                        if (($x - $cx) ** 2 + ($y - $cy) ** 2 <= $r * $r + 1e-7) $count++;
                    }
                    $ans = max($ans, $count);
                }
            }
        }
        return $ans;
    }
}
