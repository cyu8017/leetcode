// LeetCode 0149 - Max Points on a Line
// https://leetcode.com/problems/max-points-on-a-line/

export function maxPoints(points: number[][]): number {
  if (points.length <= 2) return points.length;

  let best = 1;
  for (let i = 0; i < points.length; i += 1) {
    const slopes = new Map<string, number>();
    let localBest = 1;

    for (let j = i + 1; j < points.length; j += 1) {
      let dx = points[j][0] - points[i][0];
      let dy = points[j][1] - points[i][1];
      const divisor = gcd(dx, dy);
      dx /= divisor;
      dy /= divisor;
      if (dx < 0 || (dx === 0 && dy < 0)) {
        dx = -dx;
        dy = -dy;
      }

      const slope = `${dx},${dy}`;
      const count = (slopes.get(slope) ?? 0) + 1;
      slopes.set(slope, count);
      localBest = Math.max(localBest, count + 1);
    }
    best = Math.max(best, localBest);
  }

  return best;
}

function gcd(a: number, b: number): number {
  a = Math.abs(a);
  b = Math.abs(b);
  while (b !== 0) {
    [a, b] = [b, a % b];
  }
  return a;
}