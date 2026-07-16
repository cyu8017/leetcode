// LeetCode 0505 - The Maze II
// https://leetcode.com/problems/the-maze-ii/

public class Solution {
    public int ShortestDistance(int[][] maze, int[] start, int[] destination) {
        int rows = maze.Length;
        int cols = maze[0].Length;
        int targetRow = destination[0];
        int targetCol = destination[1];
        int[][] directions = {
            new[] { -1, 0 },
            new[] { 1, 0 },
            new[] { 0, -1 },
            new[] { 0, 1 },
        };
        Dictionary<string, int> best = new();
        PriorityQueue<State, State> heap = new();
        heap.Enqueue(new State(0, start[0], start[1]), new State(0, start[0], start[1]));

        while (heap.Count > 0) {
            State current = heap.Dequeue();
            if (current.Row == targetRow && current.Col == targetCol) {
                return current.Dist;
            }
            string stateKey = $"{current.Row},{current.Col}";
            if (best.TryGetValue(stateKey, out int recorded) && recorded <= current.Dist) {
                continue;
            }
            best[stateKey] = current.Dist;
            foreach (int[] direction in directions) {
                int dr = direction[0];
                int dc = direction[1];
                int nextRow = current.Row;
                int nextCol = current.Col;
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
                if (nextRow == current.Row && nextCol == current.Col) {
                    continue;
                }
                int newDist = current.Dist + traveled;
                string targetKey = $"{nextRow},{nextCol}";
                if (!best.TryGetValue(targetKey, out int existing) || newDist < existing) {
                    State next = new State(newDist, nextRow, nextCol);
                    heap.Enqueue(next, next);
                }
            }
        }
        return -1;
    }

    private sealed record State(int Dist, int Row, int Col) : IComparable<State> {
        public int CompareTo(State? other) {
            if (other is null) {
                return 1;
            }
            return Dist.CompareTo(other.Dist);
        }
    }
}
