<?php
class Solution {
    function kthSmallest($mat, $k) {
        $sums = [0];
        foreach ($mat as $row) {
            $heap = new SplMinHeap();
            $heap->insert([$sums[0] + $row[0], 0, 0]);
            $merged = [];
            $seen = [];
            while (!$heap->isEmpty() && count($merged) < $k) {
                [$value, $i, $j] = $heap->extract();
                $key = "$i,$j";
                if (isset($seen[$key])) continue;
                $seen[$key] = true;
                $merged[] = $value;
                if ($j + 1 < count($row)) $heap->insert([$sums[$i] + $row[$j + 1], $i, $j + 1]);
                if ($j === 0 && $i + 1 < count($sums)) $heap->insert([$sums[$i + 1] + $row[0], $i + 1, 0]);
            }
            $sums = $merged;
        }
        return $sums[$k - 1];
    }
}
