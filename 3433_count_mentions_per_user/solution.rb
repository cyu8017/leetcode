# LeetCode 3433 - Count Mentions Per User
# https://leetcode.com/problems/count-mentions-per-user/

# @param {Integer} number_of_users
# @param {String[][]} events
# @return {Integer[]}
def count_mentions(number_of_users, events)
  events = events.sort_by { |e| [e[1].to_i, e[0] == "OFFLINE" ? 0 : 1] }
  online = Array.new(number_of_users, true)
  offline_until = Array.new(number_of_users, 0)
  ans = Array.new(number_of_users, 0)
  events.each do |e|
    t = e[1].to_i
    (0...number_of_users).each do |i|
      online[i] = true if !online[i] && offline_until[i] <= t
    end
    if e[0] == "OFFLINE"
      uid = e[2].to_i
      online[uid] = false
      offline_until[uid] = t + 60
    else
      msg = e[2]
      if msg == "ALL"
        (0...number_of_users).each { |i| ans[i] += 1 }
      elsif msg == "HERE"
        (0...number_of_users).each { |i| ans[i] += 1 if online[i] }
      else
        msg.split(" ").each do |part|
          uid = part[2..].to_i
          ans[uid] += 1
        end
      end
    end
  end
  ans
end
