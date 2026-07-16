// LeetCode 0406 - Queue Reconstruction by Height
export function reconstructQueue(people: number[][]): number[][] {
    people.sort((a, b) => (a[0] === b[0] ? a[1] - b[1] : b[0] - a[0]));
    const queue: number[][] = [];
    for (const person of people) {
        queue.splice(person[1], 0, person);
    }
    return queue;
}
