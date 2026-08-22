// LeetCode 0458 - Poor Pigs
// https://leetcode.com/problems/poor-pigs/

int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
    int states = minutesToTest / minutesToDie + 1;
    int pigs = 0;
    long long capacity = 1;
    while (capacity < buckets) {
        pigs++;
        capacity *= states;
    }
    return pigs;
}
