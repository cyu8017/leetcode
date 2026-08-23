// LeetCode 0818 - Race Car
// https://leetcode.com/problems/race-car/

import java.util.*;

class Solution {
    public int racecar(int target) {
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[] {0, 1, 0});
        Set<Long> seen = new HashSet<>();
        seen.add(key(0, 1));
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int pos = cur[0], speed = cur[1], steps = cur[2];
            if (pos == target) return steps;
            int nxtPos = pos + speed, nxtSpeed = speed * 2;
            if (!seen.contains(key(nxtPos, nxtSpeed)) && Math.abs(nxtPos) < target * 2) {
                seen.add(key(nxtPos, nxtSpeed));
                queue.offer(new int[] {nxtPos, nxtSpeed, steps + 1});
            }
            int revSpeed = speed > 0 ? -1 : 1;
            if (seen.add(key(pos, revSpeed))) {
                queue.offer(new int[] {pos, revSpeed, steps + 1});
            }
        }
        return -1;
    }

    private long key(int pos, int speed) {
        return ((long) pos << 20) ^ (speed & 0xfffffL);
    }
}
