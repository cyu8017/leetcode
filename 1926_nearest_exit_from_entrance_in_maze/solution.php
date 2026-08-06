<?php
class Solution {
    /**
     * @param String[][] $maze
     * @param Integer[] $entrance
     * @return Integer
     */
    function nearestExit($maze, $entrance) {
        $m = count($maze);
        $n = count($maze[0]);
        $er = $entrance[0];
        $ec = $entrance[1];
        $q = [[$er, $ec, 0]];
        $maze[$er][$ec] = '+';
        $dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        $qi = 0;
        while ($qi < count($q)) {
            [$r, $c, $d] = $q[$qi++];
            foreach ($dirs as $dir) {
                $nr = $r + $dir[0];
                $nc = $c + $dir[1];
                if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $maze[$nr][$nc] === '.') {
                    if ($nr === 0 || $nr === $m - 1 || $nc === 0 || $nc === $n - 1) {
                        return $d + 1;
                    }
                    $maze[$nr][$nc] = '+';
                    $q[] = [$nr, $nc, $d + 1];
                }
            }
        }
        return -1;
    }
}
