// LeetCode 2126 - Destroying Asteroids
// https://leetcode.com/problems/destroying-asteroids/

export function asteroidsDestroyed(mass: number, asteroids: number[]): boolean {
    asteroids = asteroids.slice().sort((a, b) => a - b);
    let cur = mass;
    for (const a of asteroids) {
        if (cur < a) return false;
        cur += a;
    }
    return true;
}
