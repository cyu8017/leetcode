# LeetCode 2225 - Find Players With Zero or One Losses
# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

# @param {Integer[][]} matches
# @return {Integer[][]}
def find_winners(matches)
  lose = Hash.new(0)
  seen = {}
  matches.each do |w, l|
    seen[w] = true
    seen[l] = true
    lose[l] += 1
  end
  zero = []
  one = []
  seen.each_key do |p|
    cnt = lose[p]
    if cnt == 0
      zero << p
    elsif cnt == 1
      one << p
    end
  end
  [zero.sort, one.sort]
end
