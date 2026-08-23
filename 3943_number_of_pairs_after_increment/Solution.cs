// LeetCode 3943 - Number of Pairs After Increment
// https://leetcode.com/problems/number-of-pairs-after-increment/

using System;
using System.Collections.Generic;

public class Solution {
    public long[] NumberOfPairs(int[] nums1, int[] nums2, int[][] queries) {
        const int blockSize = 225;
        int n = nums2.Length;
        int blocks = (n + blockSize - 1) / blockSize;
        int[] lazy = new int[blocks];
        var freq = new Dictionary<int, int>[blocks];
        for (int b = 0; b < blocks; b++) freq[b] = new Dictionary<int, int>();
        void Rebuild(int b) {
            freq[b].Clear();
            int end = Math.Min((b + 1) * blockSize, n);
            for (int i = b * blockSize; i < end; i++) {
                if (!freq[b].ContainsKey(nums2[i])) freq[b][nums2[i]] = 0;
                freq[b][nums2[i]]++;
            }
        }
        void Push(int b) {
            if (lazy[b] != 0) {
                int end = Math.Min((b + 1) * blockSize, n);
                for (int i = b * blockSize; i < end; i++) nums2[i] += lazy[b];
                lazy[b] = 0;
            }
        }
        for (int b = 0; b < blocks; b++) Rebuild(b);
        var fixedMap = new Dictionary<int, int>();
        foreach (int x in nums1) {
            if (!fixedMap.ContainsKey(x)) fixedMap[x] = 0;
            fixedMap[x]++;
        }
        var answer = new List<long>();
        foreach (var q in queries) {
            if (q[0] == 1) {
                int l = q[1], r = q[2], delta = q[3];
                int first = l / blockSize, last = r / blockSize;
                if (first == last) {
                    Push(first);
                    for (int i = l; i <= r; i++) nums2[i] += delta;
                    Rebuild(first);
                    continue;
                }
                Push(first);
                for (int i = l; i < (first + 1) * blockSize; i++) nums2[i] += delta;
                Rebuild(first);
                Push(last);
                for (int i = last * blockSize; i <= r; i++) nums2[i] += delta;
                Rebuild(last);
                for (int b = first + 1; b < last; b++) lazy[b] += delta;
            } else {
                long total = 0;
                foreach (var kv in fixedMap) {
                    int a = kv.Key, countA = kv.Value;
                    int target = q[1] - a;
                    for (int b = 0; b < blocks; b++) {
                        int key = target - lazy[b];
                        if (freq[b].TryGetValue(key, out int c)) total += (long)countA * c;
                    }
                }
                answer.Add(total);
            }
        }
        return answer.ToArray();
    }
}
