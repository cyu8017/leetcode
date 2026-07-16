// LeetCode 0444 - Sequence Reconstruction
// https://leetcode.com/problems/sequence-reconstruction/

export class Solution {
    sequenceReconstruction(nums: number[], sequences: number[][]): boolean {
        const indegree = new Map(nums.map((value) => [value, 0]));
        const graph = new Map(nums.map((value) => [value, new Set<number>()]));
        const seenEdges = new Set<string>();

        for (const sequence of sequences) {
            for (let index = 0; index < sequence.length - 1; index += 1) {
                const left = sequence[index];
                const right = sequence[index + 1];
                const edge = `${left},${right}`;
                if (seenEdges.has(edge)) continue;
                seenEdges.add(edge);
                graph.get(left)!.add(right);
                indegree.set(right, indegree.get(right)! + 1);
            }
        }

        const queue = nums.filter((value) => indegree.get(value) === 0);
        const order: number[] = [];
        while (queue.length > 0) {
            if (queue.length > 1) return false;
            const node = queue.shift()!;
            order.push(node);
            for (const neighbor of graph.get(node)!) {
                indegree.set(neighbor, indegree.get(neighbor)! - 1);
                if (indegree.get(neighbor) === 0) {
                    queue.push(neighbor);
                }
            }
        }

        return order.length === nums.length && order.every((value, index) => value === nums[index]);
    }
}
