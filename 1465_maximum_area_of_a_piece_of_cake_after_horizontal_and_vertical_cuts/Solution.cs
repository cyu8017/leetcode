// LeetCode 1465 - Maximum Area Of A Piece Of Cake After Horizontal And Vertical Cuts
// https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

using System;
using System.Linq;
public class Solution {
    public int MaxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        var hs = new int[horizontalCuts.Length + 2];
        hs[0] = 0; hs[hs.Length - 1] = h;
        Array.Copy(horizontalCuts, 0, hs, 1, horizontalCuts.Length); Array.Sort(hs);
        var vs = new int[verticalCuts.Length + 2];
        vs[0] = 0; vs[vs.Length - 1] = w;
        Array.Copy(verticalCuts, 0, vs, 1, verticalCuts.Length); Array.Sort(vs);
        long maxH = 0, maxV = 0;
        for (int i = 1; i < hs.Length; i++) maxH = Math.Max(maxH, hs[i] - hs[i - 1]);
        for (int i = 1; i < vs.Length; i++) maxV = Math.Max(maxV, vs[i] - vs[i - 1]);
        return (int)(maxH * maxV % 1000000007);
    }
}
