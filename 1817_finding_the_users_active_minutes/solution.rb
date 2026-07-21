
# @param {Integer[][]} logs
# @param {Integer} k
# @return {Integer[]}
def finding_users_active_minutes(logs, k)
  user_minutes = Hash.new { |h, key| h[key] = {} }
  logs.each do |user_id, minute|
    user_minutes[user_id][minute] = true
  end

  answer = Array.new(k, 0)
  user_minutes.each_value do |minutes|
    uam = minutes.length
    answer[uam - 1] += 1 if uam <= k
  end
  answer
end
