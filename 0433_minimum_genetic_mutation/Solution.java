// LeetCode 0433 - Minimum Genetic Mutation
// https://leetcode.com/problems/minimum-genetic-mutation/

import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int minMutation(String startGene, String endGene, String[] bank) {
        if (startGene.equals(endGene)) {
            return 0;
        }

        Set<String> valid = new HashSet<>();
        for (String gene : bank) {
            valid.add(gene);
        }
        if (!valid.contains(endGene)) {
            return -1;
        }

        ArrayDeque<String> queue = new ArrayDeque<>();
        ArrayDeque<Integer> stepsQueue = new ArrayDeque<>();
        queue.offer(startGene);
        stepsQueue.offer(0);
        Set<String> visited = new HashSet<>();
        visited.add(startGene);
        String genes = "ACGT";

        while (!queue.isEmpty()) {
            String gene = queue.poll();
            int steps = stepsQueue.poll();
            if (gene.equals(endGene)) {
                return steps;
            }
            char[] chars = gene.toCharArray();
            for (int index = 0; index < chars.length; index++) {
                char original = chars[index];
                for (int j = 0; j < genes.length(); j++) {
                    char letter = genes.charAt(j);
                    if (letter == original) {
                        continue;
                    }
                    chars[index] = letter;
                    String candidate = new String(chars);
                    if (valid.contains(candidate) && !visited.contains(candidate)) {
                        visited.add(candidate);
                        queue.offer(candidate);
                        stepsQueue.offer(steps + 1);
                    }
                }
                chars[index] = original;
            }
        }

        return -1;
    }
}
