# LeetCode 3921 - Score Validator
# https://leetcode.com/problems/score-validator/

# @param {String[]} events
# @return {Integer[]}
def score_validator(events)
  score = 0
  counter = 0
  events.each do |event_str|
    is_num = !event_str.empty?
    num = 0
    start = 0
    if is_num && event_str[0] == "-"
      start = 1
    end
    (start...event_str.length).each do |i|
      if event_str[i] < "0" || event_str[i] > "9"
        is_num = false
        break
      end
      num = num * 10 + (event_str[i].ord - 48)
    end
    if is_num && !(start == 1 && event_str.length == 1)
      num = -num if start == 1
      score += num
    elsif event_str == "W"
      counter += 1
      break if counter == 10
    else
      score += 1
    end
  end
  [score, counter]
end
