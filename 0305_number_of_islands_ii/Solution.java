// LeetCode 0305 - Number of Islands II
// https://leetcode.com/problems/number-of-islands-ii/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private final Map<Integer, Integer> parent = new HashMap<>();
    private final Map<Integer, Integer> rank = new HashMap<>();

    public List<Integer> numIslands2(int m, int n, int[][] positions) {
        List<Integer> result = new ArrayList<>();
        int islands = 0;
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        for (int[] position : positions) {
            int row = position[0];
            int col = position[1];
            int index = row * n + col;
            if (parent.containsKey(index)) {
                result.add(islands);
                continue;
            }
            parent.put(index, index);
            rank.put(index, 0);
            islands++;

            for (int[] direction : directions) {
                int nextRow = row + direction[0];
                int nextCol = col + direction[1];
                if (nextRow < 0 || nextRow >= m || nextCol < 0 || nextCol >= n) {
                    continue;
                }
                int neighbor = nextRow * n + nextCol;
                if (parent.containsKey(neighbor) && union(index, neighbor)) {
                    islands--;
                }
            }
            result.add(islands);
        }
        return result;
    }

    private int find(int index) {
        int root = parent.get(index);
        if (root != index) {
            root = find(root);
            parent.put(index, root);
        }
        return root;
    }

    private boolean union(int left, int right) {
        int rootLeft = find(left);
        int rootRight = find(right);
        if (rootLeft == rootRight) {
            return false;
        }
        int leftRank = rank.get(rootLeft);
        int rightRank = rank.get(rootRight);
        if (leftRank < rightRank) {
            parent.put(rootLeft, rootRight);
        } else if (leftRank > rightRank) {
            parent.put(rootRight, rootLeft);
        } else {
            parent.put(rootRight, rootLeft);
            rank.put(rootLeft, leftRank + 1);
        }
        return true;
    }
}
