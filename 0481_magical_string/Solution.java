// LeetCode 0481 - Magical String
// https://leetcode.com/problems/magical-string/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int magicalString(int n) {
        if (n == 0) {
            return 0;
        }
        List<Integer> seq = new ArrayList<>(Arrays.asList(1, 2, 2));
        int index = 2;
        while (seq.size() < n) {
            int next = seq.get(seq.size() - 1) == 2 ? 1 : 2;
            if (seq.get(index) == 1) {
                seq.add(next);
            } else {
                seq.add(next);
                if (seq.size() < n) {
                    seq.add(next);
                }
            }
            index += 1;
        }
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (seq.get(i) == 1) {
                count += 1;
            }
        }
        return count;
    }
}
