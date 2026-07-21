// LeetCode 1900 - The Earliest and Latest Rounds Where Players Compete
// https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

public class Solution {
    private int first;
    private int second;
    private readonly Dictionary<string, int[]> memo = new();

    public int[] EarliestAndLatest(int n, int firstPlayer, int secondPlayer) {
        first = firstPlayer;
        second = secondPlayer;
        memo.Clear();
        var players = new List<int>();
        for (int i = 1; i <= n; i++) {
            players.Add(i);
        }
        return Dfs(players);
    }

    private int[] Dfs(List<int> players) {
        string key = string.Join(",", players);
        if (memo.TryGetValue(key, out int[]? cached)) {
            return cached;
        }

        int count = players.Count;
        int firstIndex = players.IndexOf(first);
        int secondIndex = players.IndexOf(second);
        if (firstIndex + secondIndex == count - 1) {
            var result = new[] { 1, 1 };
            memo[key] = result;
            return result;
        }

        var choices = new List<List<int>>();
        for (int index = 0; index < count / 2; index++) {
            int left = players[index];
            int right = players[count - 1 - index];
            if (left == first || left == second) {
                choices.Add(new List<int> { left });
            } else if (right == first || right == second) {
                choices.Add(new List<int> { right });
            } else {
                choices.Add(new List<int> { left, right });
            }
        }
        if (count % 2 == 1) {
            choices.Add(new List<int> { players[count / 2] });
        }

        int earliest = int.MaxValue / 2;
        int latest = 0;
        var picks = new List<int>();

        void Explore(int i) {
            if (i == choices.Count) {
                var winners = new List<int>(picks);
                winners.Sort();
                int[] next = Dfs(winners);
                earliest = Math.Min(earliest, next[0] + 1);
                latest = Math.Max(latest, next[1] + 1);
                return;
            }
            foreach (int pick in choices[i]) {
                picks.Add(pick);
                Explore(i + 1);
                picks.RemoveAt(picks.Count - 1);
            }
        }

        Explore(0);
        var answer = new[] { earliest, latest };
        memo[key] = answer;
        return answer;
    }
}
