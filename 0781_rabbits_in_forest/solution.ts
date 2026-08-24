// LeetCode 0781 - Rabbits in Forest
// https://leetcode.com/problems/rabbits-in-forest/

export function numRabbits(answers: number[]): number {
    const counts = new Map();
    for (const answer of answers) counts.set(answer, (counts.get(answer) || 0) + 1);
    let total = 0;
    for (const [key, value] of counts) {
        const group = key + 1;
        const groups = Math.floor((value + group - 1) / group);
        total += groups * group;
    }
    return total;
}
