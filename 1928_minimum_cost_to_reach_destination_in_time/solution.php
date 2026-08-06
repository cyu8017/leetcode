<?php
class Solution {
    /**
     * @param Integer $maxTime
     * @param Integer[][] $edges
     * @param Integer[] $passingFee
     * @return Integer
     */
    function minCost($maxTime, $edges, $passingFee) {
        $n = count($passingFee);
        $graph = array_fill(0, $n, []);
        foreach ($edges as $e) {
            $graph[$e[0]][] = [$e[1], $e[2]];
            $graph[$e[1]][] = [$e[0], $e[2]];
        }

        $minTime = array_fill(0, $n, $maxTime + 1);
        $pq = [];
        $this->push($pq, [$passingFee[0], 0, 0]);

        while (!empty($pq)) {
            [$cost, $time, $u] = $this->pop($pq);
            if ($time >= $minTime[$u]) {
                continue;
            }
            $minTime[$u] = $time;
            if ($u === $n - 1) {
                return $cost;
            }
            foreach ($graph[$u] as $e) {
                $v = $e[0];
                $nt = $time + $e[1];
                if ($nt <= $maxTime && $nt < $minTime[$v]) {
                    $this->push($pq, [$cost + $passingFee[$v], $nt, $v]);
                }
            }
        }
        return -1;
    }

    private function push(&$heap, $item) {
        $heap[] = $item;
        $i = count($heap) - 1;
        while ($i > 0) {
            $p = ($i - 1) >> 1;
            if ($heap[$p][0] <= $heap[$i][0]) {
                break;
            }
            $tmp = $heap[$p];
            $heap[$p] = $heap[$i];
            $heap[$i] = $tmp;
            $i = $p;
        }
    }

    private function pop(&$heap) {
        $top = $heap[0];
        $last = array_pop($heap);
        if (empty($heap)) {
            return $top;
        }
        $heap[0] = $last;
        $i = 0;
        $n = count($heap);
        while (true) {
            $l = $i * 2 + 1;
            $r = $l + 1;
            $s = $i;
            if ($l < $n && $heap[$l][0] < $heap[$s][0]) {
                $s = $l;
            }
            if ($r < $n && $heap[$r][0] < $heap[$s][0]) {
                $s = $r;
            }
            if ($s === $i) {
                break;
            }
            $tmp = $heap[$i];
            $heap[$i] = $heap[$s];
            $heap[$s] = $tmp;
            $i = $s;
        }
        return $top;
    }
}
