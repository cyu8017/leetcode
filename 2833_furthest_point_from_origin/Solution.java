// LeetCode 2833 - Furthest Point From Origin
// https://leetcode.com/problems/furthest-point-from-origin/

class Solution {
    public int furthestDistanceFromOrigin(String moves) {
        int L = 0, R = 0, u = 0;
        for (int i = 0; i < moves.length(); i++) {
            char c = moves.charAt(i);
            if (c == 'L') L++;
            else if (c == 'R') R++;
            else u++;
        }
        return Math.abs(L - R) + u;
    }
}
