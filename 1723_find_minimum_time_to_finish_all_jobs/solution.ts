// LeetCode 1723 - Find Minimum Time to Finish All Jobs
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

function minimumTimeRequired(jobs: number[], k: number): number {
    jobs.sort((a, b) => b - a);
    const loads: number[] = new Array(k).fill(0);
    let best = jobs.reduce((sum, job) => sum + job, 0);

    const backtrack = (i: number): void => {
        if (i === jobs.length) {
            best = Math.min(best, Math.max(...loads));
            return;
        }
        const seen = new Set<number>();
        for (let worker = 0; worker < k; worker++) {
            if (seen.has(loads[worker])) {
                continue;
            }
            if (loads[worker] + jobs[i] >= best) {
                continue;
            }
            seen.add(loads[worker]);
            loads[worker] += jobs[i];
            backtrack(i + 1);
            loads[worker] -= jobs[i];
            if (loads[worker] === 0) {
                break;
            }
        }
    };

    backtrack(0);
    return best;
}
