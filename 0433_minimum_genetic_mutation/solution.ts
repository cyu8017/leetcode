// LeetCode 0433 - Minimum Genetic Mutation
// https://leetcode.com/problems/minimum-genetic-mutation/

export class Solution {
    minMutation(startGene: string, endGene: string, bank: string[]): number {
        if (startGene === endGene) return 0;
        const valid = new Set(bank);
        if (!valid.has(endGene)) return -1;

        const genes = "ACGT";
        const queue: [string, number][] = [[startGene, 0]];
        const visited = new Set<string>([startGene]);

        while (queue.length > 0) {
            const [gene, steps] = queue.shift()!;
            if (gene === endGene) return steps;
            const chars = gene.split("");
            for (let index = 0; index < chars.length; index += 1) {
                const original = chars[index];
                for (const letter of genes) {
                    if (letter === original) continue;
                    chars[index] = letter;
                    const candidate = chars.join("");
                    if (valid.has(candidate) && !visited.has(candidate)) {
                        visited.add(candidate);
                        queue.push([candidate, steps + 1]);
                    }
                }
                chars[index] = original;
            }
        }

        return -1;
    }
}
