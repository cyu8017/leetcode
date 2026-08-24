# LeetCode 2868 - The Wording Game
# https://leetcode.com/problems/the-wording-game/

# @param {String[]} a
# @param {String[]} b
# @return {Boolean}
def can_alice_win(a, b)
  closely_greater = lambda do |w, z|
    w > z && (w[0] == z[0] || w[0].ord == z[0].ord + 1)
  end

  i = 1
  j = 0
  last = a[0]
  alice = false
  loop do
    if alice
      i += 1 while i < a.length && !closely_greater.call(a[i], last)
      return false if i == a.length

      last = a[i]
      i += 1
    else
      j += 1 while j < b.length && !closely_greater.call(b[j], last)
      return true if j == b.length

      last = b[j]
      j += 1
    end
    alice = !alice
  end
end
