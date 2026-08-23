// LeetCode 3492 - Maximum Containers on a Ship
// https://leetcode.com/problems/maximum-containers-on-a-ship/

class Solution {
    public int maxContainers(int n, int w, int maxWeight) {
        int cap = n * n;
        int byW = maxWeight / w;
        return cap < byW ? cap : byW;
    }
}
