// LeetCode 1538 - Guess the Majority in a Hidden Array
// https://leetcode.com/problems/guess-the-majority-in-a-hidden-array/

class ArrayReader {
    private final int[] nums;

    ArrayReader(int[] nums) {
        this.nums = nums;
    }

    public int query(int a, int b, int c, int d) {
        int ones = nums[a] + nums[b] + nums[c] + nums[d];
        if (ones == 0 || ones == 4) {
            return 4;
        }
        if (ones == 1 || ones == 3) {
            return 2;
        }
        return 0;
    }

    public int length() {
        return nums.length;
    }
}

class Solution {
    public int guessMajority(int[] nums) {
        return guessMajority(new ArrayReader(nums));
    }

    public int guessMajority(ArrayReader reader) {
        int n = reader.length();
        int firstFour = reader.query(0, 1, 2, 3);
        int shifted = reader.query(1, 2, 3, 4);
        int same = 1;
        int different = 0;
        int differentIndex = -1;
        int laterDifferent = -1;
        boolean fourSame = firstFour == shifted;
        if (fourSame) {
            same++;
        } else {
            different++;
            differentIndex = 4;
        }
        int[][] checks = {
            {0, 2, 3, 4},
            {0, 1, 3, 4},
            {0, 1, 2, 4}
        };
        for (int index = 0; index < checks.length; index++) {
            int[] args = checks[index];
            if (reader.query(args[0], args[1], args[2], args[3]) == shifted) {
                same++;
            } else {
                different++;
                differentIndex = index + 1;
            }
        }
        for (int i = 5; i < n; i++) {
            boolean iSameAsFour = reader.query(1, 2, 3, i) == shifted;
            if (iSameAsFour == fourSame) {
                same++;
            } else {
                different++;
                differentIndex = i;
                if (laterDifferent == -1) {
                    laterDifferent = i;
                }
            }
        }
        if (same == different) {
            return -1;
        }
        return same > different ? 0 : (laterDifferent != -1 ? laterDifferent : differentIndex);
    }
}
