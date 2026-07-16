// LeetCode 0358 - Rearrange String k Distance Apart

// https://leetcode.com/problems/rearrange-string-k-distance-apart/



using System.Collections.Generic;



public class Solution {

    public string RearrangeString(string s, int k) {

        Dictionary<char, int> counts = new();

        foreach (char ch in s) {

            counts[ch] = counts.GetValueOrDefault(ch) + 1;

        }



        int maxFreq = 0;

        int maxFreqChars = 0;

        foreach (int count in counts.Values) {

            if (count > maxFreq) {

                maxFreq = count;

                maxFreqChars = 1;

            } else if (count == maxFreq) {

                maxFreqChars++;

            }

        }



        if ((s.Length - maxFreqChars) < (maxFreq - 1) * (k - 1)) {

            return "";

        }



        PriorityQueue<(int count, char ch), (int count, char ch)> heap = new();

        foreach (KeyValuePair<char, int> entry in counts) {

            heap.Enqueue((-entry.Value, entry.Key), (-entry.Value, entry.Key));

        }



        Queue<(int count, char ch, int readyAt)> queue = new();

        List<char> result = new();

        int index = 0;



        while (heap.Count > 0 || queue.Count > 0) {

            while (queue.Count > 0 && queue.Peek().readyAt <= index) {

                var item = queue.Dequeue();

                heap.Enqueue((item.count, item.ch), (item.count, item.ch));

            }



            if (heap.Count == 0) {

                return "";

            }



            var current = heap.Dequeue();

            result.Add(current.ch);

            if (current.count + 1 < 0) {

                queue.Enqueue((current.count + 1, current.ch, index + k));

            }

            index++;

        }



        return new string(result.ToArray());

    }

}
