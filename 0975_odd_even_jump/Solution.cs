// LeetCode 0975 - Odd Even Jump
// https://leetcode.com/problems/odd-even-jump/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int OddEvenJumps(int[] arr) {
        int n = arr.Length;
        int[] nextHigher = new int[n], nextLower = new int[n];
        int[] order = Enumerable.Range(0, n).ToArray();
        Array.Sort(order, (i, j) => arr[i] == arr[j] ? i.CompareTo(j) : arr[i].CompareTo(arr[j]));
        var stack = new List<int>();
        foreach (int i in order) {
            while (stack.Count > 0 && stack[stack.Count - 1] < i) {
                nextHigher[stack[stack.Count - 1]] = i;
                stack.RemoveAt(stack.Count - 1);
            }
            stack.Add(i);
        }
        stack.Clear();
        Array.Sort(order, (i, j) => arr[i] == arr[j] ? i.CompareTo(j) : arr[j].CompareTo(arr[i]));
        foreach (int i in order) {
            while (stack.Count > 0 && stack[stack.Count - 1] < i) {
                nextLower[stack[stack.Count - 1]] = i;
                stack.RemoveAt(stack.Count - 1);
            }
            stack.Add(i);
        }
        bool[] odd = new bool[n], even = new bool[n];
        odd[n - 1] = even[n - 1] = true;
        for (int i = n - 2; i >= 0; i--) {
            if (nextHigher[i] != 0) odd[i] = even[nextHigher[i]];
            if (nextLower[i] != 0) even[i] = odd[nextLower[i]];
        }
        return odd.Count(x => x);
    }
}
