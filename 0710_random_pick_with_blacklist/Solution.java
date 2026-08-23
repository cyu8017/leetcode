// LeetCode 0710 - Random Pick with Blacklist
// https://leetcode.com/problems/random-pick-with-blacklist/

import java.util.*;

class Solution {
    private final int size;
    private final Map<Integer, Integer> mapping = new HashMap<>();
    private final Random rand = new Random();

    public Solution(int n, int[] blacklist) {
        size = n - blacklist.length;
        Set<Integer> black = new HashSet<>();
        for (int b : blacklist) black.add(b);
        int white = size;
        for (int b : blacklist) {
            if (b < size) {
                while (black.contains(white)) white++;
                mapping.put(b, white++);
            }
        }
    }

    public int pick() {
        int index = rand.nextInt(size);
        return mapping.getOrDefault(index, index);
    }
}
