// LeetCode 1311 - Get Watched Videos By Your Friends
// https://leetcode.com/problems/get-watched-videos-by-your-friends/

function watchedVideosByFriends(watchedVideos: string[][], friends: number[][], id: number, level: number): string[] {
    const queue = [[id, 0]], seen = new Set([id]), people = [];
    while (queue.length) {
        const [person, distance] = queue.shift();
        if (distance === level) {
            people.push(person);
            continue;
        }
        for (const friend of friends[person]) {
            if (!seen.has(friend)) {
                seen.add(friend);
                queue.push([friend, distance + 1]);
            }
        }
    }
    const counts = new Map();
    for (const person of people) {
        for (const video of watchedVideos[person]) {
            counts.set(video, (counts.get(video) || 0) + 1);
        }
    }
    return [...counts.keys()].sort((a, b: any): any => counts.get(a) - counts.get(b) || (a < b ? -1 : a > b ? 1 : 0));
}
