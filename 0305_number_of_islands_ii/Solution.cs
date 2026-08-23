// LeetCode 0305 - Number of Islands II
// https://leetcode.com/problems/number-of-islands-ii/

using System.Collections.Generic;

public class Solution {
    private readonly Dictionary<int, int> parent = new();
    private readonly Dictionary<int, int> rank = new();

    public IList<int> NumIslands2(int m, int n, int[][] positions) {
        List<int> result = new();
        int islands = 0;
        int[][] directions = {
            new[] { 1, 0 },
            new[] { -1, 0 },
            new[] { 0, 1 },
            new[] { 0, -1 },
        };

        foreach (int[] position in positions) {
            int row = position[0];
            int col = position[1];
            int index = row * n + col;
            if (parent.ContainsKey(index)) {
                result.Add(islands);
                continue;
            }
            parent[index] = index;
            rank[index] = 0;
            islands++;

            foreach (int[] direction in directions) {
                int nextRow = row + direction[0];
                int nextCol = col + direction[1];
                if (nextRow < 0 || nextRow >= m || nextCol < 0 || nextCol >= n) {
                    continue;
                }
                int neighbor = nextRow * n + nextCol;
                if (parent.ContainsKey(neighbor) && Union(index, neighbor)) {
                    islands--;
                }
            }
            result.Add(islands);
        }
        return result;
    }

    private int Find(int index) {
        int root = parent[index];
        if (root != index) {
            root = Find(root);
            parent[index] = root;
        }
        return root;
    }

    private bool Union(int left, int right) {
        int rootLeft = Find(left);
        int rootRight = Find(right);
        if (rootLeft == rootRight) {
            return false;
        }
        int leftRank = rank[rootLeft];
        int rightRank = rank[rootRight];
        if (leftRank < rightRank) {
            parent[rootLeft] = rootRight;
        } else if (leftRank > rightRank) {
            parent[rootRight] = rootLeft;
        } else {
            parent[rootRight] = rootLeft;
            rank[rootLeft] = leftRank + 1;
        }
        return true;
    }
}
