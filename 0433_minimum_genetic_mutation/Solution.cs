// LeetCode 0433 - Minimum Genetic Mutation
// https://leetcode.com/problems/minimum-genetic-mutation/

using System.Collections.Generic;

public class Solution {
    public int MinMutation(string startGene, string endGene, string[] bank) {
        if (startGene == endGene) {
            return 0;
        }

        HashSet<string> valid = new HashSet<string>(bank);
        if (!valid.Contains(endGene)) {
            return -1;
        }

        Queue<(string gene, int steps)> queue = new Queue<(string, int)>();
        queue.Enqueue((startGene, 0));
        HashSet<string> visited = new HashSet<string> { startGene };
        string genes = "ACGT";

        while (queue.Count > 0) {
            (string gene, int steps) = queue.Dequeue();
            if (gene == endGene) {
                return steps;
            }
            char[] chars = gene.ToCharArray();
            for (int index = 0; index < chars.Length; index++) {
                char original = chars[index];
                foreach (char letter in genes) {
                    if (letter == original) {
                        continue;
                    }
                    chars[index] = letter;
                    string candidate = new string(chars);
                    if (valid.Contains(candidate) && !visited.Contains(candidate)) {
                        visited.Add(candidate);
                        queue.Enqueue((candidate, steps + 1));
                    }
                }
                chars[index] = original;
            }
        }

        return -1;
    }
}
