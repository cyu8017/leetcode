<?php
// LeetCode 0488 - Zuma Game
// https://leetcode.com/problems/zuma-game/

class Solution {
    /** @var array<string, int> */
    private $memo = [];

    /**
     * @param string $board
     * @param string $hand
     * @return int
     */
    function findMinStep($board, $hand) {
        return $this->find_min_step($board, $hand);
    }

    /**
     * @param string $board
     * @param string $hand
     * @return int
     */
    function find_min_step($board, $hand) {
        $this->memo = [];
        $result = $this->dfs($board, $hand);
        return $result === PHP_INT_MAX ? -1 : $result;
    }

    private function shrink(string $s): string {
        $length = strlen($s);
        $index = 0;
        while ($index < $length) {
            $end = $index;
            while ($end < $length && $s[$end] === $s[$index]) {
                $end++;
            }
            if ($end - $index >= 3) {
                return $this->shrink(substr($s, 0, $index) . substr($s, $end));
            }
            $index = $end;
        }
        return $s;
    }

    private function dfs(string $board, string $hand): int {
        $key = $board . '|' . $hand;
        if (array_key_exists($key, $this->memo)) {
            return $this->memo[$key];
        }

        $board = $this->shrink($board);
        if ($board === '') {
            return 0;
        }

        $best = PHP_INT_MAX;
        $boardLength = strlen($board);
        $handLength = strlen($hand);
        for ($insert = 0; $insert <= $boardLength; $insert++) {
            for ($pick = 0; $pick < $handLength; $pick++) {
                $color = $hand[$pick];
                if ($insert < $boardLength && $board[$insert] === $color) {
                    continue;
                }
                if ($insert > 0 && $board[$insert - 1] === $color) {
                    continue;
                }
                $newBoard = $this->shrink(substr($board, 0, $insert) . $color . substr($board, $insert));
                if ($newBoard === $board) {
                    continue;
                }
                $newHand = substr($hand, 0, $pick) . substr($hand, $pick + 1);
                $steps = $this->dfs($newBoard, $newHand);
                if ($steps !== PHP_INT_MAX) {
                    $best = min($best, $steps + 1);
                }
            }
        }
        $this->memo[$key] = $best;
        return $best;
    }
}
