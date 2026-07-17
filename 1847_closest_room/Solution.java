// LeetCode 1847 - Closest Room
// https://leetcode.com/problems/closest-room/

import java.util.Arrays;
import java.util.Comparator;
import java.util.TreeSet;

class Solution {
    public int[] closestRoom(int[][] rooms, int[][] queries) {
        Arrays.sort(rooms, Comparator.comparingInt(room -> room[1]));

        int[][] indexedQueries = new int[queries.length][3];
        for (int i = 0; i < queries.length; i++) {
            indexedQueries[i][0] = i;
            indexedQueries[i][1] = queries[i][0];
            indexedQueries[i][2] = queries[i][1];
        }
        Arrays.sort(indexedQueries, Comparator.comparingInt(query -> -query[2]));

        TreeSet<Integer> availableIds = new TreeSet<>();
        int roomIndex = rooms.length - 1;
        int[] answer = new int[queries.length];
        Arrays.fill(answer, -1);

        for (int[] query : indexedQueries) {
            int queryIndex = query[0];
            int preferred = query[1];
            int minSize = query[2];

            while (roomIndex >= 0 && rooms[roomIndex][1] >= minSize) {
                availableIds.add(rooms[roomIndex][0]);
                roomIndex--;
            }

            if (availableIds.isEmpty()) {
                continue;
            }

            int bestId = -1;
            int bestDist = Integer.MAX_VALUE;

            Integer higher = availableIds.ceiling(preferred);
            if (higher != null) {
                bestId = higher;
                bestDist = Math.abs(higher - preferred);
            }

            Integer lower = availableIds.floor(preferred);
            if (lower != null) {
                int dist = Math.abs(lower - preferred);
                if (dist < bestDist || (dist == bestDist && lower < bestId)) {
                    bestId = lower;
                }
            }

            answer[queryIndex] = bestId;
        }

        return answer;
    }
}
