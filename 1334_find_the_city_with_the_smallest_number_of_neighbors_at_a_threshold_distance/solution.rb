# LeetCode 1334 - Find The City With The Smallest Number Of Neighbors At A Threshold Distance
# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

def find_the_city(n, edges, distance_threshold)
  inf = 10**15
  dist = Array.new(n) { Array.new(n, inf) }
  n.times { |i| dist[i][i] = 0 }
  edges.each do |a, b, weight|
    dist[a][b] = weight
    dist[b][a] = weight
  end
  n.times do |k|
    n.times do |i|
      n.times do |j|
        dist[i][j] = [dist[i][j], dist[i][k] + dist[k][j]].min
      end
    end
  end
  (0...n).min_by { |city| [dist[city].count { |d| d <= distance_threshold }, -city] }
end
