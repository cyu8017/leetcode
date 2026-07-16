// LeetCode 0277 - Find the Celebrity
// https://leetcode.com/problems/find-the-celebrity/

export class Solution {
    findCelebrity(this: Solution & { knows(a: number, b: number): boolean }, n: number): number {
        let candidate = 0;
        for (let person = 1; person < n; person++) {
            if (this.knows(candidate, person)) {
                candidate = person;
            }
        }
        for (let person = 0; person < n; person++) {
            if (person === candidate) {
                continue;
            }
            if (this.knows(candidate, person) || !this.knows(person, candidate)) {
                return -1;
            }
        }
        return candidate;
    }
}

export function knows(_a: number, _b: number): boolean {
    return false;
}

const solution = new Solution();
export const findCelebrity = solution.findCelebrity.bind(
    Object.assign(solution, { knows }),
);
