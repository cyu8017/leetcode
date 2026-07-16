// LeetCode 0466 - Count The Repetitions
// https://leetcode.com/problems/count-the-repetitions/

public class Solution {
    public int GetMaxRepetitions(string s1, int n1, string s2, int n2) {
        if (string.IsNullOrEmpty(s2)) {
            return 0;
        }

        int index = 0;
        int s2Count = 0;
        Dictionary<int, int[]> record = new();

        for (int repeat = 0; repeat < n1; repeat++) {
            foreach (char ch in s1) {
                if (ch == s2[index]) {
                    index++;
                    if (index == s2.Length) {
                        index = 0;
                        s2Count++;
                    }
                }
            }
            if (record.TryGetValue(index, out int[]? previous)) {
                int previousRepeat = previous[0];
                int previousCount = previous[1];
                int cycle = repeat - previousRepeat;
                int countCycle = s2Count - previousCount;
                int remaining = n1 - repeat - 1;
                s2Count += (remaining / cycle) * countCycle;
                if (repeat + (remaining / cycle) * cycle >= n1 - 1) {
                    break;
                }
            }
            record[index] = new[] { repeat, s2Count };
        }

        return s2Count / n2;
    }
}
