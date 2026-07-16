// LeetCode 0470 - Implement Rand10() Using Rand7()
// https://leetcode.com/problems/implement-rand10-using-rand7/

class Rand7 {
    private static java.util.Iterator<Integer> sequence;

    static void setSequence(int[] values) {
        java.util.List<Integer> items = new java.util.ArrayList<>();
        for (int value : values) {
            items.add(value);
        }
        sequence = items.iterator();
    }

    static int rand7() {
        return sequence.next();
    }
}

class Solution {
    public int rand10() {
        while (true) {
            int num = (Rand7.rand7() - 1) * 7 + Rand7.rand7();
            if (num <= 40) {
                return (num - 1) % 10 + 1;
            }
        }
    }
}
