// LeetCode 0458 - Poor Pigs
// https://leetcode.com/problems/poor-pigs/

class Solution {
    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        int states = minutesToTest / minutesToDie + 1;
        int pigs = 0;
        int capacity = 1;
        while (capacity < buckets) {
            pigs++;
            capacity *= states;
        }
        return pigs;
    }
}
