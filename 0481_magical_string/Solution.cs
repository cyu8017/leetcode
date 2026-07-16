// LeetCode 0481 - Magical String
// https://leetcode.com/problems/magical-string/

public class Solution {
    public int MagicalString(int n) {
        if (n == 0) {
            return 0;
        }
        List<int> seq = new() { 1, 2, 2 };
        int index = 2;
        while (seq.Count < n) {
            int next = seq[^1] == 2 ? 1 : 2;
            if (seq[index] == 1) {
                seq.Add(next);
            } else {
                seq.Add(next);
                if (seq.Count < n) {
                    seq.Add(next);
                }
            }
            index += 1;
        }
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (seq[i] == 1) {
                count += 1;
            }
        }
        return count;
    }
}
