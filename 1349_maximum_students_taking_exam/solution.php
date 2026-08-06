<?php
class Solution {
    function maxStudents($seats) {
        $rows = count($seats);
        $cols = count($seats[0]);
        $validRows = [];
        foreach ($seats as $row) {
            $available = 0;
            for ($c = 0; $c < $cols; $c++) {
                if ($row[$c] === ".") $available |= 1 << $c;
            }
            $masks = [];
            for ($mask = 0; $mask < (1 << $cols); $mask++) {
                if (($mask & ~$available) === 0 && ($mask & ($mask << 1)) === 0) $masks[] = $mask;
            }
            $validRows[] = $masks;
        }
        $dp = [0 => 0];
        foreach ($validRows as $masks) {
            $nxt = [];
            foreach ($masks as $mask) {
                foreach ($dp as $previous => $count) {
                    if (($mask & ($previous << 1)) === 0 && ($mask & ($previous >> 1)) === 0) {
                        $nxt[$mask] = max($nxt[$mask] ?? 0, $count + substr_count(decbin($mask), "1"));
                    }
                }
            }
            $dp = $nxt;
        }
        return max($dp);
    }
}
