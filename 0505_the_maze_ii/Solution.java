// LeetCode 0505 - The Maze II
// https://leetcode.com/problems/the-maze-ii/

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    public int shortestDistance(int[][] maze, int[] start, int[] destination) {
        int rows = maze.length;
        int cols = maze[0].length;
        int targetRow = destination[0];
        int targetCol = destination[1];
        int[][] directions = {
            { -1, 0 },
            { 1, 0 },
            { 0, -1 },
            { 0, 1 },
        };
        Map<String, Integer> best = new HashMap<>();
        PriorityQueue<State> heap = new PriorityQueue<>();
        heap.offer(new State(0, start[0], start[1]));

        while (!heap.isEmpty()) {
            State current = heap.poll();
            if (current.row == targetRow && current.col == targetCol) {
                return current.dist;
            }
            String stateKey = current.row + "," + current.col;
            if (best.getOrDefault(stateKey, Integer.MAX_VALUE) <= current.dist) {
                continue;
            }
            best.put(stateKey, current.dist);
            for (int[] direction : directions) {
                int dr = direction[0];
                int dc = direction[1];
                int nextRow = current.row;
                int nextCol = current.col;
                int traveled = 0;
                while (nextRow + dr >= 0
                        && nextRow + dr < rows
                        && nextCol + dc >= 0
                        && nextCol + dc < cols
                        && maze[nextRow + dr][nextCol + dc] == 0) {
                    nextRow += dr;
                    nextCol += dc;
                    traveled++;
                }
                if (nextRow == current.row && nextCol == current.col) {
                    continue;
                }
                int newDist = current.dist + traveled;
                String targetKey = nextRow + "," + nextCol;
                if (newDist < best.getOrDefault(targetKey, Integer.MAX_VALUE)) {
                    heap.offer(new State(newDist, nextRow, nextCol));
                }
            }
        }
        return -1;
    }

    private static class State implements Comparable<State> {
        final int dist;
        final int row;
        final int col;

        State(int dist, int row, int col) {
            this.dist = dist;
            this.row = row;
            this.col = col;
        }

        @Override
        public int compareTo(State other) {
            return Integer.compare(this.dist, other.dist);
        }
    }
}
