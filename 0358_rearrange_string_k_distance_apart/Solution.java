// LeetCode 0358 - Rearrange String k Distance Apart

// https://leetcode.com/problems/rearrange-string-k-distance-apart/



import java.util.ArrayDeque;

import java.util.Deque;

import java.util.HashMap;

import java.util.Map;

import java.util.PriorityQueue;



class Solution {

    public String rearrangeString(String s, int k) {

        Map<Character, Integer> counts = new HashMap<>();

        for (char ch : s.toCharArray()) {

            counts.put(ch, counts.getOrDefault(ch, 0) + 1);

        }



        int maxFreq = 0;

        int maxFreqChars = 0;

        for (int count : counts.values()) {

            if (count > maxFreq) {

                maxFreq = count;

                maxFreqChars = 1;

            } else if (count == maxFreq) {

                maxFreqChars++;

            }

        }



        if ((s.length() - maxFreqChars) < (maxFreq - 1) * (k - 1)) {

            return "";

        }



        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> {

            if (a[0] != b[0]) {

                return Integer.compare(a[0], b[0]);

            }

            return Integer.compare(a[1], b[1]);

        });



        for (Map.Entry<Character, Integer> entry : counts.entrySet()) {

            heap.offer(new int[] {-entry.getValue(), entry.getKey()});

        }



        Deque<int[]> queue = new ArrayDeque<>();

        StringBuilder result = new StringBuilder();

        int index = 0;



        while (!heap.isEmpty() || !queue.isEmpty()) {

            while (!queue.isEmpty() && queue.peek()[2] <= index) {

                heap.offer(queue.poll());

            }



            if (heap.isEmpty()) {

                return "";

            }



            int[] current = heap.poll();

            result.append((char) current[1]);

            if (current[0] + 1 < 0) {

                queue.offerLast(new int[] {current[0] + 1, current[1], index + k});

            }

            index++;

        }



        return result.toString();

    }

}
