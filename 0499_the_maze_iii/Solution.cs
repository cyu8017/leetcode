// LeetCode 0499 - The Maze III
// https://leetcode.com/problems/the-maze-iii/

public class Solution {
    public string FindShortestWay(int[][] maze, int[] ball, int[] hole) {
        int rows = maze.Length;
        int cols = maze[0].Length;
        int holeRow = hole[0];
        int holeCol = hole[1];
        int[][] directions = {
            new[] { 1, 0 },
            new[] { 0, -1 },
            new[] { 0, 1 },
            new[] { -1, 0 },
        };
        string[] labels = { "d", "l", "r", "u" };
        Dictionary<string, Best> best = new();
        PriorityQueue<State, State> heap = new();
        heap.Enqueue(new State(0, "", ball[0], ball[1]), new State(0, "", ball[0], ball[1]));

        while (heap.Count > 0) {
            State current = heap.Dequeue();
            string stateKey = $"{current.Row},{current.Col}";
            if (best.TryGetValue(stateKey, out Best? recorded)) {
                if (current.Dist > recorded.Dist) {
                    continue;
                }
                if (current.Dist == recorded.Dist
                    && string.Compare(current.Path, recorded.Path, StringComparison.Ordinal) >= 0) {
                    continue;
                }
            }
            best[stateKey] = new Best(current.Dist, current.Path);

            if (current.Row == holeRow && current.Col == holeCol) {
                return current.Path;
            }

            for (int direction = 0; direction < directions.Length; direction++) {
                int dr = directions[direction][0];
                int dc = directions[direction][1];
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
                    if (nextRow == holeRow && nextCol == holeCol) {
                        break;
                    }
                }
                if (nextRow == current.Row && nextCol == current.Col) {
                    continue;
                }
                int newDist = current.Dist + traveled;
                string newPath = current.Path + labels[direction];
                string targetKey = $"{nextRow},{nextCol}";
                if (!best.TryGetValue(targetKey, out Best? existing)
                    || newDist < existing.Dist
                    || (newDist == existing.Dist
                        && string.Compare(newPath, existing.Path, StringComparison.Ordinal) < 0)) {
                    State next = new State(newDist, newPath, nextRow, nextCol);
                    heap.Enqueue(next, next);
                }
            }
        }
        return "impossible";
    }

    private sealed record Best(int Dist, string Path);

    private sealed record State(int Dist, string Path, int Row, int Col) : IComparable<State> {
        public int CompareTo(State? other) {
            if (other is null) {
                return 1;
            }
            if (Dist != other.Dist) {
                return Dist.CompareTo(other.Dist);
            }
            return string.Compare(Path, other.Path, StringComparison.Ordinal);
        }
    }
}
