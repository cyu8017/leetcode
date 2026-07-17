// LeetCode 1900 - The Earliest and Latest Rounds Where Players Compete
// https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private int first;
    private int second;
    private Map<String, int[]> memo = new HashMap<>();

    public int[] earliestAndLatest(int n, int firstPlayer, int secondPlayer) {
        first = firstPlayer;
        second = secondPlayer;
        memo.clear();
        int[] players = new int[n];
        for (int i = 0; i < n; i++) {
            players[i] = i + 1;
        }
        return dfs(players);
    }

    private int[] dfs(int[] players) {
        String key = Arrays.toString(players);
        if (memo.containsKey(key)) {
            return memo.get(key);
        }

        int count = players.length;
        int firstIndex = indexOf(players, first);
        int secondIndex = indexOf(players, second);
        if (firstIndex + secondIndex == count - 1) {
            int[] result = {1, 1};
            memo.put(key, result);
            return result;
        }

        List<int[]> choices = new ArrayList<>();
        for (int i = 0; i < count / 2; i++) {
            int left = players[i];
            int right = players[count - 1 - i];
            if (left == first || left == second) {
                choices.add(new int[] {left});
            } else if (right == first || right == second) {
                choices.add(new int[] {right});
            } else {
                choices.add(new int[] {left, right});
            }
        }
        if (count % 2 == 1) {
            choices.add(new int[] {players[count / 2]});
        }

        int earliest = Integer.MAX_VALUE;
        int latest = 0;
        int[] indices = new int[choices.size()];
        while (true) {
            int[] winners = new int[choices.size()];
            for (int i = 0; i < choices.size(); i++) {
                winners[i] = choices.get(i)[indices[i]];
            }
            Arrays.sort(winners);
            int[] round = dfs(winners);
            earliest = Math.min(earliest, round[0] + 1);
            latest = Math.max(latest, round[1] + 1);

            int pos = choices.size() - 1;
            while (pos >= 0) {
                indices[pos]++;
                if (indices[pos] < choices.get(pos).length) {
                    break;
                }
                indices[pos] = 0;
                pos--;
            }
            if (pos < 0) {
                break;
            }
        }

        int[] answer = {earliest, latest};
        memo.put(key, answer);
        return answer;
    }

    private int indexOf(int[] players, int value) {
        for (int i = 0; i < players.length; i++) {
            if (players[i] == value) {
                return i;
            }
        }
        return -1;
    }
}
