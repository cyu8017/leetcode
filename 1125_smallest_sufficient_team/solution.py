# LeetCode 1125 - Smallest Sufficient Team
# https://leetcode.com/problems/smallest-sufficient-team/

from functools import lru_cache


class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        skill_id = {skill: i for i, skill in enumerate(req_skills)}
        person_masks = []
        for skills in people:
            mask = 0
            for skill in skills:
                mask |= 1 << skill_id[skill]
            person_masks.append(mask)
        target = (1 << len(req_skills)) - 1

        @lru_cache(None)
        def dp(state: int) -> tuple[int, ...]:
            if state == target:
                return ()
            best: tuple[int, ...] | None = None
            for idx, mask in enumerate(person_masks):
                next_state = state | mask
                if next_state == state:
                    continue
                team = (idx,) + dp(next_state)
                if best is None or len(team) < len(best):
                    best = team
            return best or ()

        return list(dp(0))
