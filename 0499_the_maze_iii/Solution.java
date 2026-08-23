// LeetCode 0499 - The Maze III
// https://leetcode.com/problems/the-maze-iii/

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    public String findShortestWay(int[][] maze, int[] ball, int[] hole) {
        int rows = maze.length;
        int cols = maze[0].length;
        int holeRow = hole[0];
        int holeCol = hole[1];
        int[][] directions = {
            { 1, 0 },
            { 0, -1 },
            { 0, 1 },
            { -1, 0 },
        };
        String[] labels = { "d", "l", "r", "u" };

        Map<String, Best> best = new HashMap<>();
        PriorityQueue<State> heap = new PriorityQueue<>();
        heap.offer(new State(0, "", ball[0], ball[1]));

        while (!heap.isEmpty()) {
            State current = heap.poll();
            String stateKey = current.row + "," + current.col;
            Best recorded = best.get(stateKey);
            if (recorded != null) {
                if (current.dist > recorded.dist) {
                    continue;
                }
                if (current.dist == recorded.dist && current.path.compareTo(recorded.path) >= 0) {
                    continue;
                }
            }
            best.put(stateKey, new Best(current.dist, current.path));

            if (current.row == holeRow && current.col == holeCol) {
                return current.path;
            }

            for (int direction = 0; direction < directions.length; direction++) {
                int dr = directions[direction][0];
                int dc = directions[direction][1];
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
                    if (nextRow == holeRow && nextCol == holeCol) {
                        break;
                    }
                }
                if (nextRow == current.row && nextCol == current.col) {
                    continue;
                }
                int newDist = current.dist + traveled;
                String newPath = current.path + labels[direction];
                String targetKey = nextRow + "," + nextCol;
                Best existing = best.get(targetKey);
                if (existing == null
                        || newDist < existing.dist
                        || (newDist == existing.dist && newPath.compareTo(existing.path) < 0)) {
                    heap.offer(new State(newDist, newPath, nextRow, nextCol));
                }
            }
        }
        return "impossible";
    }

    private static class Best {
        final int dist;
        final String path;

        Best(int dist, String path) {
            this.dist = dist;
            this.path = path;
        }
    }

    private static class State implements Comparable<State> {
        final int dist;
        final String path;
        final int row;
        final int col;

        State(int dist, String path, int row, int col) {
            this.dist = dist;
            this.path = path;
            this.row = row;
            this.col = col;
        }

        @Override
        public int compareTo(State other) {
            if (this.dist != other.dist) {
                return Integer.compare(this.dist, other.dist);
            }
            return this.path.compareTo(other.path);
        }
    }
}
