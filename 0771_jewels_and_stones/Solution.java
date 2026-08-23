// LeetCode 0771 - Jewels and Stones
// https://leetcode.com/problems/jewels-and-stones/

import java.util.*;

class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        Set<Character> jewelSet = new HashSet<>();
        for (char ch : jewels.toCharArray()) jewelSet.add(ch);
        int count = 0;
        for (char stone : stones.toCharArray()) if (jewelSet.contains(stone)) count++;
        return count;
    }
}
