# LeetCode 1847 - Closest Room
# https://leetcode.com/problems/closest-room/

import bisect


class Solution:
    def closestRoom(self, rooms: list[list[int]], queries: list[list[int]]) -> list[int]:
        rooms.sort(key=lambda room: room[1])
        indexed_queries = sorted(
            enumerate(queries),
            key=lambda item: -item[1][1],
        )

        available_ids: list[int] = []
        room_index = len(rooms) - 1
        answer = [-1] * len(queries)

        for query_index, (preferred, min_size) in indexed_queries:
            while room_index >= 0 and rooms[room_index][1] >= min_size:
                bisect.insort(available_ids, rooms[room_index][0])
                room_index -= 1

            if not available_ids:
                continue

            pos = bisect.bisect_left(available_ids, preferred)
            best_id = -1
            best_dist = float("inf")

            if pos < len(available_ids):
                room_id = available_ids[pos]
                dist = abs(room_id - preferred)
                if dist < best_dist or (dist == best_dist and room_id < best_id):
                    best_id = room_id
                    best_dist = dist

            if pos > 0:
                room_id = available_ids[pos - 1]
                dist = abs(room_id - preferred)
                if dist < best_dist or (dist == best_dist and room_id < best_id):
                    best_id = room_id

            answer[query_index] = best_id

        return answer
