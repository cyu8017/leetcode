// LeetCode 0575 - Distribute Candies
// https://leetcode.com/problems/distribute-candies/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int distributeCandies(int[] candyType) {
        Set<Integer> unique = new HashSet<>();
        for (int candy : candyType) {
            unique.add(candy);
        }
        return Math.min(unique.size(), candyType.length / 2);
    }
}
