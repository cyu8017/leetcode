// LeetCode 1705 - Maximum Number of Eaten Apples
// https://leetcode.com/problems/maximum-number-of-eaten-apples/

public class Solution {
    public int EatenApples(int[] apples, int[] days) {
        var heap = new PriorityQueue<int[], int>();
        int n = apples.Length;
        int day = 0;
        int eaten = 0;
        while (day < n || heap.Count > 0) {
            if (day < n && apples[day] > 0) {
                int expire = day + days[day];
                heap.Enqueue(new int[] { expire, apples[day] }, expire);
            }
            while (heap.Count > 0 && heap.Peek()[0] <= day) {
                heap.Dequeue();
            }
            if (heap.Count > 0) {
                int[] top = heap.Dequeue();
                eaten++;
                if (top[1] > 1) {
                    heap.Enqueue(new int[] { top[0], top[1] - 1 }, top[0]);
                }
            }
            day++;
        }
        return eaten;
    }
}
