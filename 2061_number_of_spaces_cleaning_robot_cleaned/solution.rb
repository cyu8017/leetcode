# LeetCode 2061 - Number of Spaces Cleaning Robot Cleaned
# https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/

# @param {Integer[][]} room
# @return {Integer}
def number_of_clean_rooms(room)
  m = room.length
  n = room[0].length
  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  vis = {}
  cleaned = { 0 => true }
  r = c = d = 0
  loop do
    state = r * 10000 + c * 10 + d
    break if vis[state]

    vis[state] = true
    nr = r + dirs[d][0]
    nc = c + dirs[d][1]
    if nr.between?(0, m - 1) && nc.between?(0, n - 1) && room[nr][nc].zero?
      r = nr
      c = nc
      cleaned[(r << 32) ^ (c & 0xFFFFFFFF)] = true
    else
      d = (d + 1) % 4
    end
  end
  cleaned.length
end

alias solve number_of_clean_rooms
