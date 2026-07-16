from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)
        loads = [0] * k
        best = sum(jobs)

        def backtrack(i: int) -> None:
            nonlocal best
            if i == len(jobs):
                best = min(best, max(loads))
                return
            seen = set()
            for worker in range(k):
                if loads[worker] in seen:
                    continue
                if loads[worker] + jobs[i] >= best:
                    continue
                seen.add(loads[worker])
                loads[worker] += jobs[i]
                backtrack(i + 1)
                loads[worker] -= jobs[i]
                if loads[worker] == 0:
                    break

        backtrack(0)
        return best
