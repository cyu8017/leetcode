// LeetCode 0407 - Trapping Rain Water II
// https://leetcode.com/problems/trapping-rain-water-ii/

class Solution {
    /**
     * @param Integer[][] $heightMap
     * @return Integer
     */
    function trapRainWater($heightMap) {
        return $this->trap_rain_water($heightMap);
    }

    /**
     * @param Integer[][] $heightMap
     * @return Integer
     */
    function trap_rain_water($heightMap) {
        if ($heightMap === null || count($heightMap) === 0 || count($heightMap[0]) === 0) {
            return 0;
        }

        $rows = count($heightMap);
        $cols = count($heightMap[0]);
        if ($rows < 3 || $cols < 3) {
            return 0;
        }

        $visited = array_fill(0, $rows, array_fill(0, $cols, false));
        $heap = [];

        for ($row = 0; $row < $rows; $row++) {
            for ($col = 0; $col < $cols; $col++) {
                if ($row === 0 || $row === $rows - 1 || $col === 0 || $col === $cols - 1) {
                    $this->heapPush($heap, [$heightMap[$row][$col], $row, $col]);
                    $visited[$row][$col] = true;
                }
            }
        }

        $trapped = 0;
        $directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];

        while (count($heap) > 0) {
            [$height, $row, $col] = $this->heapPop($heap);
            foreach ($directions as [$dr, $dc]) {
                $nextRow = $row + $dr;
                $nextCol = $col + $dc;
                if ($nextRow < 0 || $nextRow >= $rows || $nextCol < 0 || $nextCol >= $cols) {
                    continue;
                }
                if ($visited[$nextRow][$nextCol]) {
                    continue;
                }

                $visited[$nextRow][$nextCol] = true;
                $nextHeight = $heightMap[$nextRow][$nextCol];
                $trapped += max(0, $height - $nextHeight);
                $this->heapPush($heap, [max($height, $nextHeight), $nextRow, $nextCol]);
            }
        }

        return $trapped;
    }

    /**
     * @param array<int, array{0: int, 1: int, 2: int}> $heap
     * @param array{0: int, 1: int, 2: int} $item
     * @return void
     */
    private function heapPush(&$heap, $item) {
        $heap[] = $item;
        $index = count($heap) - 1;
        while ($index > 0) {
            $parent = intdiv($index - 1, 2);
            if ($heap[$parent][0] <= $heap[$index][0]) {
                break;
            }
            $tmp = $heap[$index];
            $heap[$index] = $heap[$parent];
            $heap[$parent] = $tmp;
            $index = $parent;
        }
    }

    /**
     * @param array<int, array{0: int, 1: int, 2: int}> $heap
     * @return array{0: int, 1: int, 2: int}
     */
    private function heapPop(&$heap) {
        $top = $heap[0];
        $last = array_pop($heap);
        if (count($heap) === 0) {
            return $top;
        }
        $heap[0] = $last;
        $index = 0;
        while (true) {
            $smallest = $index;
            $left = $index * 2 + 1;
            $right = $index * 2 + 2;
            if ($left < count($heap) && $heap[$left][0] < $heap[$smallest][0]) {
                $smallest = $left;
            }
            if ($right < count($heap) && $heap[$right][0] < $heap[$smallest][0]) {
                $smallest = $right;
            }
            if ($smallest === $index) {
                break;
            }
            $tmp = $heap[$index];
            $heap[$index] = $heap[$smallest];
            $heap[$smallest] = $tmp;
            $index = $smallest;
        }
        return $top;
    }
}
