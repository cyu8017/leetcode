// LeetCode 0358 - Rearrange String k Distance Apart
// https://leetcode.com/problems/rearrange-string-k-distance-apart/

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function rearrangeString($s, $k) {
        return $this->rearrange_string($s, $k);
    }

    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function rearrange_string($s, $k) {
        $counts = [];
        $length = strlen($s);
        for ($index = 0; $index < $length; $index++) {
            $char = $s[$index];
            if (!array_key_exists($char, $counts)) {
                $counts[$char] = 0;
            }
            $counts[$char]++;
        }

        $maxFreq = max($counts);
        $maxFreqChars = 0;
        foreach ($counts as $count) {
            if ($count === $maxFreq) {
                $maxFreqChars++;
            }
        }

        if (($length - $maxFreqChars) < ($maxFreq - 1) * ($k - 1)) {
            return '';
        }

        $heap = [];
        foreach ($counts as $char => $count) {
            $this->heapPush($heap, [-$count, $char]);
        }

        $queue = [];
        $result = '';
        $index = 0;

        while (count($heap) > 0 || count($queue) > 0) {
            while (count($queue) > 0 && $queue[0][2] <= $index) {
                $entry = array_shift($queue);
                $this->heapPush($heap, [$entry[0], $entry[1]]);
            }

            if (count($heap) === 0) {
                return '';
            }

            $entry = $this->heapPop($heap);
            $count = $entry[0];
            $char = $entry[1];
            $result .= $char;
            if ($count + 1 < 0) {
                $queue[] = [$count + 1, $char, $index + $k];
            }
            $index++;
        }

        return $result;
    }

    /**
     * @param array<int, array{0: int, 1: string}> $heap
     * @param array{0: int, 1: string} $item
     */
    private function heapPush(&$heap, $item) {
        $heap[] = $item;
        $index = count($heap) - 1;
        while ($index > 0) {
            $parent = intdiv($index - 1, 2);
            if ($heap[$parent] <= $heap[$index]) {
                break;
            }
            $tmp = $heap[$index];
            $heap[$index] = $heap[$parent];
            $heap[$parent] = $tmp;
            $index = $parent;
        }
    }

    /**
     * @param array<int, array{0: int, 1: string}> $heap
     * @return array{0: int, 1: string}
     */
    private function heapPop(&$heap) {
        $top = $heap[0];
        $last = array_pop($heap);
        if (count($heap) > 0) {
            $heap[0] = $last;
            $index = 0;
            while (true) {
                $smallest = $index;
                $left = 2 * $index + 1;
                $right = $left + 1;
                if ($left < count($heap) && $heap[$left] < $heap[$smallest]) {
                    $smallest = $left;
                }
                if ($right < count($heap) && $heap[$right] < $heap[$smallest]) {
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
        }
        return $top;
    }
}
