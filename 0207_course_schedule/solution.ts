// LeetCode 0207 - Course Schedule
// https://leetcode.com/problems/course-schedule/

export function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    const graph: number[][] = Array.from({ length: numCourses }, () => []);
    const indegree = new Array<number>(numCourses).fill(0);
    for (const [course, prerequisite] of prerequisites) {
        graph[prerequisite].push(course);
        indegree[course] += 1;
    }

    const queue: number[] = [];
    for (let course = 0; course < numCourses; course += 1) {
        if (indegree[course] === 0) queue.push(course);
    }

    let taken = 0;
    for (let front = 0; front < queue.length; front += 1) {
        const course = queue[front];
        taken += 1;
        for (const next of graph[course]) {
            indegree[next] -= 1;
            if (indegree[next] === 0) queue.push(next);
        }
    }
    return taken === numCourses;
}