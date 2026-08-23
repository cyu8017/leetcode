// LeetCode 1538 - Guess the Majority in a Hidden Array
// https://leetcode.com/problems/guess-the-majority-in-a-hidden-array/

public class ArrayReader {
    private readonly int[] nums;
    public ArrayReader(int[] nums) { this.nums = nums; }
    public int Query(int a, int b, int c, int d) {
        int ones = nums[a] + nums[b] + nums[c] + nums[d];
        if (ones == 0 || ones == 4) return 4;
        if (ones == 1 || ones == 3) return 2;
        return 0;
    }
    public int Length() => nums.Length;
}

public class Solution {
    public int GuessMajority(int[] nums) => GuessMajority(new ArrayReader(nums));

    public int GuessMajority(ArrayReader reader) {
        int n = reader.Length();
        int firstFour = reader.Query(0, 1, 2, 3);
        int shifted = reader.Query(1, 2, 3, 4);
        int same = 1, different = 0, differentIndex = -1, laterDifferent = -1;
        bool fourSame = firstFour == shifted;
        if (fourSame) same++;
        else { different++; differentIndex = 4; }

        int[][] checks = { new[] { 0, 2, 3, 4 }, new[] { 0, 1, 3, 4 }, new[] { 0, 1, 2, 4 } };
        for (int index = 0; index < checks.Length; index++) {
            var args = checks[index];
            if (reader.Query(args[0], args[1], args[2], args[3]) == shifted) same++;
            else { different++; differentIndex = index + 1; }
        }
        for (int i = 5; i < n; i++) {
            bool iSameAsFour = reader.Query(1, 2, 3, i) == shifted;
            if (iSameAsFour == fourSame) same++;
            else {
                different++;
                differentIndex = i;
                if (laterDifferent == -1) laterDifferent = i;
            }
        }
        if (same == different) return -1;
        return same > different ? 0 : (laterDifferent != -1 ? laterDifferent : differentIndex);
    }
}
