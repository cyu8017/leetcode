// LeetCode 2102 - Sequentially Ordinal Rank Tracker
// https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

public class SORTracker {
    private class Loc : IComparable<Loc> {
        public string Name;
        public int Score;
        public Loc(string name, int score) { Name = name; Score = score; }
        // For min-heap of "best": smaller score first; on tie larger name first
        public int CompareTo(Loc other) {
            if (Score != other.Score) return Score.CompareTo(other.Score);
            return string.CompareOrdinal(other.Name, Name);
        }
    }

    private class LocMax : IComparable<LocMax> {
        public string Name;
        public int Score;
        public LocMax(string name, int score) { Name = name; Score = score; }
        // For max-heap of "rest": larger score first; on tie smaller name first
        public int CompareTo(LocMax other) {
            if (Score != other.Score) return other.Score.CompareTo(Score);
            return string.CompareOrdinal(Name, other.Name);
        }
    }

    // Use PriorityQueue with custom priorities mirroring C++ heaps
    private readonly PriorityQueue<(string name, int score), (int score, string name)> best =
        new PriorityQueue<(string, int), (int, string)>(Comparer<(int score, string name)>.Create((a, b) => {
            int c = a.score.CompareTo(b.score);
            if (c != 0) return c;
            return string.CompareOrdinal(b.name, a.name); // larger name first when scores equal (min-heap key)
        }));
    private readonly PriorityQueue<(string name, int score), (int scoreNeg, string name)> rest =
        new PriorityQueue<(string, int), (int, string)>(Comparer<(int scoreNeg, string name)>.Create((a, b) => {
            int c = a.scoreNeg.CompareTo(b.scoreNeg);
            if (c != 0) return c;
            return string.CompareOrdinal(a.name, b.name);
        }));
    private int k = 0;

    public SORTracker() {}

    public void Add(string name, int score) {
        best.Enqueue((name, score), (score, name));
        if (best.Count > k) {
            var t = best.Dequeue();
            rest.Enqueue(t, (-t.score, t.name));
        }
    }

    public string Get() {
        k++;
        if (rest.Count > 0) {
            var t = rest.Dequeue();
            best.Enqueue(t, (t.score, t.name));
        }
        return best.Peek().name;
    }
}
