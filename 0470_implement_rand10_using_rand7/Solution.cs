// LeetCode 0470 - Implement Rand10() Using Rand7()
// https://leetcode.com/problems/implement-rand10-using-rand7/

static class Rand7 {
    private static Queue<int>? sequence;

    public static void SetSequence(int[] values) {
        sequence = new Queue<int>(values);
    }

    public static int Rand7() {
        return sequence!.Dequeue();
    }
}

public class Solution {
    public int Rand10() {
        while (true) {
            int num = (Rand7.Rand7() - 1) * 7 + Rand7.Rand7();
            if (num <= 40) {
                return (num - 1) % 10 + 1;
            }
        }
    }
}
