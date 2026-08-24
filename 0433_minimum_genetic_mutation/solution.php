<?php
// LeetCode 0433 - Minimum Genetic Mutation
// https://leetcode.com/problems/minimum-genetic-mutation/

class Solution {
    /**
     * @param string $startGene
     * @param string $endGene
     * @param string[] $bank
     * @return int
     */
    function minMutation($startGene, $endGene, $bank) {
        return $this->min_mutation($startGene, $endGene, $bank);
    }

    /**
     * @param string $startGene
     * @param string $endGene
     * @param string[] $bank
     * @return int
     */
    function min_mutation($startGene, $endGene, $bank) {
        if ($startGene === $endGene) {
            return 0;
        }

        $valid = array_flip($bank);
        if (!isset($valid[$endGene])) {
            return -1;
        }

        $genes = "ACGT";
        $queue = [[$startGene, 0]];
        $visited = [$startGene => true];

        while (count($queue) > 0) {
            [$gene, $steps] = array_shift($queue);
            if ($gene === $endGene) {
                return $steps;
            }

            $chars = str_split($gene);
            for ($index = 0; $index < count($chars); $index++) {
                $original = $chars[$index];
                for ($letterIndex = 0; $letterIndex < 4; $letterIndex++) {
                    $letter = $genes[$letterIndex];
                    if ($letter === $original) {
                        continue;
                    }
                    $chars[$index] = $letter;
                    $candidate = implode("", $chars);
                    if (isset($valid[$candidate]) && !isset($visited[$candidate])) {
                        $visited[$candidate] = true;
                        $queue[] = [$candidate, $steps + 1];
                    }
                    $chars[$index] = $original;
                }
            }
        }

        return -1;
    }
}
