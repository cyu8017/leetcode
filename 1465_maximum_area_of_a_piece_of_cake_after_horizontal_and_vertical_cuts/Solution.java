// LeetCode 1465 - Maximum Area Of A Piece Of Cake After Horizontal And Vertical Cuts
// https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

import java.util.*;

class Solution {
    public int maxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        var hs = new int[horizontalCuts.length + 2];
        hs[0] = 0; hs[hs.length - 1] = h;
        Array.Copy(horizontalCuts, 0, hs, 1, horizontalCuts.length); Arrays.sort(hs);
        var vs = new int[verticalCuts.length + 2];
        vs[0] = 0; vs[vs.length - 1] = w;
        Array.Copy(verticalCuts, 0, vs, 1, verticalCuts.length); Arrays.sort(vs);
        long maxH = 0, maxV = 0;
        for (int i = 1; i < hs.length; i++) maxH = Math.max(maxH, hs[i] - hs[i - 1]);
        for (int i = 1; i < vs.length; i++) maxV = Math.max(maxV, vs[i] - vs[i - 1]);
        return (int)(maxH * maxV % 1000000007);
    }
}
