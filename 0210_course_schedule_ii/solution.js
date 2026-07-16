// LeetCode 0210 - Course Schedule II
// https://leetcode.com/problems/course-schedule-ii/

/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function(numCourses, prerequisites) {
    const graph = Array.from({ length: numCourses }, () => []);
    const indegree = new Array(numCourses).fill(0);
    for (const [course, prerequisite] of prerequisites) {
        graph[prerequisite].push(course);
        indegree[course] += 1;
    }

    const queue = [];
    for (let course = 0; course < numCourses; course += 1) {
        if (indegree[course] === 0) queue.push(course);
    }

    const order = [];
    for (let front = 0; front < queue.length; front += 1) {
        const course = queue[front];
        order.push(course);
        for (const next of graph[course]) {
            indegree[next] -= 1;
            if (indegree[next] === 0) queue.push(next);
        }
    }
    return order.length === numCourses ? order : [];
};