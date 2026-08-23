// LeetCode 3307 - Find the K-th Character in String Game II
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public char kthCharacter(long k, int[] operations) {
        int shift = 0;
        List<Integer> ops = new ArrayList<>();
        for (int op : operations) ops.add(op);
        while (!ops.isEmpty()) {
            int op = ops.remove(ops.size() - 1);
            long half = 1L << ops.size();
            if (k > half) {
                k -= half;
                if (op == 1) shift++;
            }
        }
        return (char) ('a' + shift % 26);
    }
}
