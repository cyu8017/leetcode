// LeetCode 0735 - Asteroid Collision
// https://leetcode.com/problems/asteroid-collision/

export function asteroidCollision(asteroids: number[]): number[] {
    const stack = [];
    for (const asteroid of asteroids) {
        let alive = true;
        while (alive && stack.length > 0 && asteroid < 0 && stack[stack.length - 1] > 0) {
            if (stack[stack.length - 1] < -asteroid) { stack.pop(); continue; }
            if (stack[stack.length - 1] === -asteroid) stack.pop();
            alive = false;
        }
        if (alive) stack.push(asteroid);
    }
    return stack;
}
